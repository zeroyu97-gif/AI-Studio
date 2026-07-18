def completion(
    self,
    path,
    line,
    character,
):

    self.transport.send(

        self.rpc.request(

            "textDocument/completion",

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