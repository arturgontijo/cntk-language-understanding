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

        default = "slot_tagging"
        grpc_method = input("Method (slot_tagging): ") if not test_flag else default
        if grpc_method == "":
            grpc_method = default

        default = "http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Example/sentences.txt"
        sentences_url = input("sentences (URL, one per line): ") if not test_flag else default
        if sentences_url == "":
            sentences_url = default

        default = "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.train.ctf?raw=true"
        train_ctf_url = input("train_ctf_url (ATIS Link): ") if not test_flag else default
        if train_ctf_url == "":
            train_ctf_url = default

        default = "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.test.ctf?raw=true"
        test_ctf_url = input("test_ctf_url (ATIS Link): ") if not test_flag else default
        if test_ctf_url == "":
            test_ctf_url = default

        default = "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/query.wl?raw=true"
        query_wl_url = input("query_wl_url (ATIS Link): ") if not test_flag else default
        if query_wl_url == "":
            query_wl_url = default

        default = "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/slots.wl?raw=true"
        slots_wl_url = input("slots_wl_url (ATIS Link): ") if not test_flag else default
        if slots_wl_url == "":
            slots_wl_url = default

        default = "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/intent.wl?raw=true"
        intent_wl_url = input("intent_wl_url (ATIS Link): ") if not test_flag else default
        if intent_wl_url == "":
            intent_wl_url = default

        default = 943
        vocab_size = input("vocab_size (943): ") if not test_flag else default
        if vocab_size == "":
            vocab_size = default

        default = 129
        num_labels = input("num_labels (129): ") if not test_flag else default
        if num_labels == "":
            num_labels = default

        default = 26
        num_intents = input("num_intents (26): ") if not test_flag else default
        if num_intents == "":
            num_intents = default

        if grpc_method == "slot_tagging":
            stub = grpc_bt_grpc.SlotTaggingStub(channel)

            request = grpc_bt_pb2.Input(
                train_ctf_url=train_ctf_url,
                test_ctf_url=test_ctf_url,
                query_wl_url=query_wl_url,
                slots_wl_url=slots_wl_url,
                intent_wl_url=intent_wl_url,
                vocab_size=vocab_size,
                num_labels=num_labels,
                num_intents=num_intents,
                sentences_url=sentences_url
            )

            response = stub.slot_tagging(request)
            print("\nresponse:")
            print("output URL: {}".format(response.output_url))
            print("model  URL: {}".format(response.model_url))
            if "Fail" in [response.output_url, response.model_url]:
                exit(1)
        else:
            print("Invalid method!")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)
