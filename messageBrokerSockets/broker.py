import socket
import threading

class Broker:
    def __init__(self, host='127.0.0.1', port=6666):
        self.host = host
        self.port = port
        self.channels = {}  
        self.senders = {}   

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Broker ascultă pe {self.host}:{self.port}")

    def handle_client(self, client_socket, addr):
        try:
            # Primul mesaj de la client: "role:sender;channel:channel_name" sau "role:receiver;channel:channel_name"
            init_message = client_socket.recv(1024).decode('utf-8')
            if not init_message:
                client_socket.close()
                return

            parts = init_message.split(';')
            role = None
            channel_name = None
            for part in parts:
                key, value = part.split(':')
                if key.strip() == 'role':
                    role = value.strip()
                elif key.strip() == 'channel':
                    channel_name = value.strip()

            if role == 'sender':
                self.handle_sender(client_socket, channel_name, addr)
            elif role == 'receiver':
                self.handle_receiver(client_socket, channel_name, addr)
            else:
                print(f"Client {addr} are un rol necunoscut: {role}")
                client_socket.close()
        except Exception as e:
            print(f"Eroare la inițializarea clientului {addr}: {e}")
            client_socket.close()

    def handle_sender(self, client_socket, channel_name, addr):
        if channel_name in self.senders:
            print(f"Canalul '{channel_name}' deja creat de un alt sender. Conexiunea va fi închisă.")
            client_socket.send("Error: Canal deja existent.".encode('utf-8'))
            client_socket.close()
            return

        # Înregistrarea senderului în canal
        self.senders[channel_name] = client_socket
        if channel_name not in self.channels:
            self.channels[channel_name] = []

        print(f"Sender {addr} a creat canalul '{channel_name}' și este conectat la broker.")

        # Ascultăm mesajele trimise de sender
        while True:
            try:
                message = client_socket.recv(1024)
                if not message:
                    print(f"Sender {addr} s-a deconectat de la canalul '{channel_name}'")
                    break
                print(f"Mesaj primit de la sender '{channel_name}': {message.decode('utf-8')}")
                self.broadcast(channel_name, message)
            except Exception as e:
                print(f"Eroare la primirea mesajului de la sender {addr}: {e}")
                break

        client_socket.close()
        del self.senders[channel_name]
        print(f"Sender {addr} a închis canalul '{channel_name}'")


    def handle_receiver(self, client_socket, channel_name, addr):
        if channel_name not in self.channels:
            print(f"Canalul '{channel_name}' nu există. Conexiunea va fi închisă pentru receiver {addr}.")
            client_socket.send("Error: Canal inexistent.".encode('utf-8'))
            client_socket.close()
            return

        self.channels[channel_name].append(client_socket)
        print(f"Receiver {addr} s-a conectat la canalul '{channel_name}'")

        try:
            while True:
                # Receiver-ul nu trimite mesaje, doar primește
                message = client_socket.recv(1024)
                if not message:
                    break
        except:
            pass

        client_socket.close()
        self.channels[channel_name].remove(client_socket)
        print(f"Receiver {addr} s-a deconectat de la canalul '{channel_name}'")

    def broadcast(self, channel_name, message):
        receivers = self.channels.get(channel_name, [])
        if not receivers:
            print(f"Nu există receiveri conectați la canalul '{channel_name}'")
        for receiver in receivers:
            try:
                print(f"Trimit mesaj la receiver în canalul '{channel_name}': {message.decode('utf-8')}")
                receiver.send(message)
            except Exception as e:
                print(f"Eroare la trimiterea mesajului către un receiver: {e}")


    def start(self):
        while True:
            client_socket, addr = self.server.accept()
            print(f"Acceptat conexiune de la {addr}")
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, addr))
            client_handler.start()

if __name__ == "__main__":
    broker = Broker()
    broker.start()
