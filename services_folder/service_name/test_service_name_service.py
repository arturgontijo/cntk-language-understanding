import sys
import grpc

# import the generated classes
import service.service_spec.cntk-language-understanding_pb2_grpc as grpc_bt_grpc
import service.service_spec.cntk-language-understanding_pb2 as grpc_bt_pb2

from service import registry

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "auto":
                test_flag = True

        # Service ONE - Arithmetic
        endpoint = input("Endpoint (localhost:{}): ".format(registry["cntk-language-understanding_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["cntk-language-understanding_service"]["grpc"])

        # Open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))

        grpc_method = input("Method (my_method): ") if not test_flag else "my_method"
        if grpc_method == "":
            grpc_method = "my_method"

        param_1 = input("Input (my_input): ") if not test_flag else "my_input"
        if param_1 == "":
            param_1 = "my_input"

        if grpc_method == "forecast":
            stub = grpc_bt_grpc.ForecastStub(channel)
            request = grpc_bt_pb2.Input(param_1=param_1)
            response = stub.forecast(request)
            print("\nresponse:")
            print("response_1           : {}".format(response.response_1))
        else:
            print("Invalid method!")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)