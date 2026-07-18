def hover(
    self,
    path,
    line,
    character,
):

    self.transport.send(

        self.rpc.request(

            "textDocument/hover",

            {

                "textDocument": {

                    "uri": path.as_uri()

                },

                "position": {

                    "line": line,

                    "character": character,

                },

            },

        )

    )