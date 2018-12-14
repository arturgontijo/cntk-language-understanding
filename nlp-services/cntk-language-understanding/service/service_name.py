[[SERVICE_PYTHON_IMPORTS]]
import logging

logging.basicConfig(level=10, format="%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
log = logging.getLogger("language_understanding")


class MyServiceClass:

    def __init__(self, my_input):
        self.my_input = my_input
        self.response = dict()

    def do_something(self):
        self.response = {"Empty": None}
        return self.response