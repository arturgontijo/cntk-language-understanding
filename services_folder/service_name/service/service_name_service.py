import sys
import logging

import grpc
import concurrent.futures as futures

import service.common
from service.cntk-language-understanding import MyServiceClass

# Importing the generated codes from buildproto.sh
import service.service_spec.cntk-language-understanding_pb2_grpc as grpc_bt_grpc
from service.service_spec.cntk-language-understanding_pb2 import Output

logging.basicConfig(level=10, format="%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
log = logging.getLogger("cntk-language-understanding_service")


# Create a class to be added to the gRPC server
# derived from the protobuf codes.
class MyServiceServicer(grpc_bt_grpc.MyServiceServicer):
    def __init__(self):
        self.my_input = ""
        self.response = ""

        log.debug("MyServiceServicer created")

    # The method that will be exposed to the snet-cli call command.
    # request: incoming data
    # context: object that provides RPC-specific information (timeout, etc).
    def forecast(self, request, context):

        try:
            # In our case, request is a Input() object (from .proto file)
            self.my_input = request.my_input

            # To respond we need to create a Output() object (from .proto file)
            self.response = Output()

            msc = MyServiceClass(self.my_input)

            tmp_response = msc.do_something()
            self.response.output_1 = tmp_response["output"].encode("utf-8")

            log.debug("do_something({})={}".format(self.my_input, self.response.output_1))
            return self.response

        except Exception as e:
            log.error(e)
            self.response = Output()
            self.response.output_1 = "Fail"
            return self.response


# The gRPC serve function.
#
# Params:
# max_workers: pool of threads to execute calls asynchronously
# port: gRPC server port
#
# Add all your classes to the server here.
# (from generated .py files by protobuf compiler)
def serve(max_workers=10, port=7777):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    grpc_bt_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port("[::]:{}".format(port))
    return server


if __name__ == "__main__":
    """
    Runs the gRPC server to communicate with the Snet Daemon.
    """
    parser = service.common.common_parser(__file__)
    args = parser.parse_args(sys.argv[1:])
    service.common.main_loop(serve, args)