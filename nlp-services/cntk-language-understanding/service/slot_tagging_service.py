import sys
import logging

import grpc
import concurrent.futures as futures

import service.common
from service.slot_tagging import SlotTagging

# Importing the generated codes from buildproto.sh
import service.service_spec.slot_tagging_pb2_grpc as grpc_bt_grpc
from service.service_spec.slot_tagging_pb2 import Output

logging.basicConfig(level=10, format="%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
log = logging.getLogger("slot_tagging_service")


# Create a class to be added to the gRPC server
# derived from the protobuf codes.
class SlotTaggingServicer(grpc_bt_grpc.SlotTaggingServicer):
    def __init__(self):
        self.train_ctf_url = ""
        self.test_ctf_url = ""
        self.query_wl_url = ""
        self.slots_wl_url = ""
        self.intent_wl_url = ""
        self.sentences_url = ""

        self.response = None

        log.debug("SlotTaggingServicer created")

    # The method that will be exposed to the snet-cli call command.
    # request: incoming data
    # context: object that provides RPC-specific information (timeout, etc).
    def slot_tagging(self, request, context):

        try:
            # In our case, request is a Input() object (from .proto file)
            self.train_ctf_url = request.train_ctf_url
            self.test_ctf_url = request.test_ctf_url
            self.query_wl_url = request.query_wl_url
            self.slots_wl_url = request.slots_wl_url
            self.intent_wl_url = request.intent_wl_url

            self.sentences_url = request.sentences_url

            # To respond we need to create a Output() object (from .proto file)
            self.response = Output()

            mst = SlotTagging(
                self.train_ctf_url,
                self.test_ctf_url,
                self.query_wl_url,
                self.slots_wl_url,
                self.intent_wl_url,
                self.sentences_url
            )

            tmp_response = mst.slot_tagging()
            self.response.output_url = str(tmp_response["output_url"]).encode("utf-8")

            log.debug("slot_tagging({})={}".format(self.sentences_url, self.response.output_url))
            return self.response

        except Exception as e:
            log.error(e)
            self.response = Output()
            self.response.output = "Fail"
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
    grpc_bt_grpc.add_SlotTaggingServicer_to_server(SlotTaggingServicer(), server)
    server.add_insecure_port("[::]:{}".format(port))
    return server


if __name__ == "__main__":
    """
    Runs the gRPC server to communicate with the Snet Daemon.
    """
    parser = service.common.common_parser(__file__)
    args = parser.parse_args(sys.argv[1:])
    service.common.main_loop(serve, args)