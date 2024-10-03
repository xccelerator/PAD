import socket
import threading

class Receiver:
    def __init__(self, host='127.0.0.1', port=6666):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        print("Conectat la broker.")

        # Solicită numele canalului
        self.channel_name = input("Introdu numele canalului la care te conectezi: ").strip()

        # Trimite mesajul inițial: "role:receiver;channel:channel_name"
        init_message = f"role:receiver;channel:{self.channel_name}"
        self.client.send(init_message.encode('utf-8'))

        # Verifică dacă s-a conectat cu succes
        response = self.client.recv(1024).decode('utf-8')
        if response.startswith("Error"):
            print(f"Eroare: {response}")
            self.client.close()
            exit()

        print(f"Conectat la canalul '{self.channel_name}'. Aștept mesaje...")

    def listen_for_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message:
                    print(f"Mesaj primit: {message}")
            except Exception as e:
                print(f"Eroare la primirea mesajului: {e}")
                break


    def start(self):
        listener = threading.Thread(target=self.listen_for_messages)
        listener.start()

if __name__ == "__main__":
    receiver = Receiver()
    receiver.start()
