import grpc
import message_broker_pb2
import message_broker_pb2_grpc

def run_receiver():
    channel = grpc.insecure_channel('localhost:50051')
    stub = message_broker_pb2_grpc.MessageBrokerStub(channel)

    channel_name = input("Introduceți numele canalului pentru a recepționa mesaje: ")

    request = message_broker_pb2.ChannelRequest(channel=channel_name)

    for message in stub.ReceiveMessages(request):
        print(f"Mesaj primit: {message.content}")

if __name__ == "__main__":
    run_receiver()
