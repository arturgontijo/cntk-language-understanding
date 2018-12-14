import sys
import grpc

# import the generated classes
import service.service_spec.slot_tagging_pb2_grpc as grpc_bt_grpc
import service.service_spec.slot_tagging_pb2 as grpc_bt_pb2

from service import registry

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "auto":
                test_flag = True

        # Service ONE - Arithmetic
        endpoint = input("Endpoint (localhost:{}): ".format(registry["slot_tagging_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["slot_tagging_service"]["grpc"])

        # Open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))

        grpc_method = input("Method (slot_tagging): ") if not test_flag else "slot_tagging"
        if grpc_method == "":
            grpc_method = "slot_tagging"

        train_ctf_url = input("train_ctf_url (ATIS Link): ") if not test_flag else "https://github.com/Microsoft/CNTK/blob/release/2.6/0/atis.train.ctf?raw=true"
        if train_ctf_url == "":
            train_ctf_url = "my_input"

        test_ctf_url = input("test_ctf_url (ATIS Link): ") if not test_flag else "https://github.com/Microsoft/CNTK/blob/release/2.6/0/atis.test.ctf?raw=true"
        if test_ctf_url == "":
            test_ctf_url = "my_input"

        query_wl_url = input("query_wl_url (ATIS Link): ") if not test_flag else "https://github.com/Microsoft/CNTK/blob/release/2.6/1/query.wl?raw=true"
        if query_wl_url == "":
            query_wl_url = "my_input"

        slots_wl_url = input("slots_wl_url (ATIS Link): ") if not test_flag else "https://github.com/Microsoft/CNTK/blob/release/2.6/1/slots.wl?raw=true"
        if slots_wl_url == "":
            slots_wl_url = "my_input"

        intent_wl_url = input("intent_wl_url (ATIS Link): ") if not test_flag else "https://github.com/Microsoft/CNTK/blob/release/2.6/1/intent.wl?raw=true"
        if intent_wl_url == "":
            intent_wl_url = "my_input"

        if grpc_method == "slot_tagging":
            stub = grpc_bt_grpc.SlotTaggingStub(channel)

            request = grpc_bt_pb2.Input(
                train_ctf_url=train_ctf_url,
                test_ctf_url=test_ctf_url,
                query_wl_url=query_wl_url,
                slots_wl_url=slots_wl_url,
                intent_wl_url=intent_wl_url,
            )

            response = stub.slot_tagging(request)
            print("\nresponse:")
            print("{}".format(response))
        else:
            print("Invalid method!")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)