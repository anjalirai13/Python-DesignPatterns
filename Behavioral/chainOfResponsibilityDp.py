class Handler:
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must Implement in subclass")


class ConcreteHandler(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print("Request is handled in handler 1".format(request))
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print("End of chain, no handler for {}".format(request))
        return True


class Client:
    def __init__(self):
        self.handler = ConcreteHandler(DefaultHandler(None))

    def delegate(self, requests):
        for r in requests:
            self.handler.handle(r)


c = Client()
requests = [2, 5, 30]
c.delegate(requests)