from .jsonrpc import JsonRPC
from .transport import LSPTransport
from .pyright import *

class LSPClient:

    def __init__(self):

        self.rpc = JsonRPC()

        self.transport = LSPTransport()

    def start(self):

        self.transport.start(

            PYRIGHT_PROGRAM,

            PYRIGHT_ARGS,

        )

        self.initialize()

    def initialize(self):

        request = self.rpc.request(

            "initialize",

            {

                "processId": None,

                "rootUri": None,

                "capabilities": {},

            },

        )

        self.transport.send(request)
        class LSPClient(QObject):

    def __init__(self):
        super().__init__()

        self.initialized = False
        self.shutdown_requested = False

        self.workspace = None

        self.rpc = JsonRPC()
        self.transport = LSPTransport()

        self.transport.messageReceived.connect(
            self._message_received
        )