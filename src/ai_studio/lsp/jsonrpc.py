class JsonRPC:

    def __init__(self):

        self.id = 0

    def request(
        self,
        method,
        params,
    ):

        self.id += 1

        return {

            "jsonrpc": "2.0",

            "id": self.id,

            "method": method,

            "params": params,

        }

    def notification(
        self,
        method,
        params,
    ):

        return {

            "jsonrpc": "2.0",

            "method": method,

            "params": params,

        }