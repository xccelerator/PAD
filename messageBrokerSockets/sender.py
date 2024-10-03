import socket
import threading

class Sender:
    def __init__(self, host='127.0.0.1', port=6666):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        print("Conectat la broker.")

        self.channel_name = input("Introdu numele canalului de creat: ").strip()

        # Trimitem mesajul inițial către broker cu detalii despre sender
        init_message = f"role:sender;channel:{self.channel_name}"
        self.client.send(init_message.encode('utf-8'))
        print(f"Mesaj inițial trimis pentru creare canal: {init_message}")

        print(f"Canalul '{self.channel_name}' a fost creat cu succes.")


    def send_message(self, message):
        try:
            self.client.send(message.encode('utf-8'))
            print(f"Mesaj trimis: {message}")
        except Exception as e:
            print(f"Eroare la trimiterea mesajului: {e}")


    def close(self):
        self.client.close()

    def run(self):
        try:
            while True:
                message = input("Introdu mesajul de trimis: ")
                self.send_message(message)
        except KeyboardInterrupt:
            self.close()
            print("\nSender-ul a fost închis.")

if __name__ == "__main__":
    sender = Sender()
    sender.run()
