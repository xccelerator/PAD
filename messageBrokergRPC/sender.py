import grpc
import message_broker_pb2
import message_broker_pb2_grpc

def run_sender():
    channel = grpc.insecure_channel('localhost:50051')
    stub = message_broker_pb2_grpc.MessageBrokerStub(channel)

    channel_name = input("Introduceți numele canalului: ")

    while True:
        message_content = input("Introduceți mesajul: ")
        message = message_broker_pb2.Message(channel=channel_name, content=message_content)
        stub.SendMessage(message)

if __name__ == "__main__":
    run_sender()
