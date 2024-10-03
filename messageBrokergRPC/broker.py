import grpc
from concurrent import futures
import time
import message_broker_pb2
import message_broker_pb2_grpc
from queue import Queue

class MessageBrokerServicer(message_broker_pb2_grpc.MessageBrokerServicer):
    def __init__(self):
        self.channels = {}

    def SendMessage(self, request, context):
        channel = request.channel
        content = request.content

        if channel in self.channels:
            for receiver in self.channels[channel]:
                receiver.put(message_broker_pb2.Message(channel=channel, content=content))

        return message_broker_pb2.Empty()

    def ReceiveMessages(self, request, context):
        channel = request.channel

        if channel not in self.channels:
            self.channels[channel] = []

        queue = Queue()
        self.channels[channel].append(queue)

        try:
            while True:
                message = queue.get()
                yield message
        except grpc.RpcError:
            self.channels[channel].remove(queue)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_broker_pb2_grpc.add_MessageBrokerServicer_to_server(MessageBrokerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Broker-ul rulează pe portul 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
