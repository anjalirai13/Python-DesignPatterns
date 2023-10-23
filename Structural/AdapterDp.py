class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong!"


class British:
    def __init__(self):
        self.name = "British"

    def speak_british(self):
        return "Hello"

class Adapter:

    def __init__(self, obj, **args):
        self._object = obj
        self.__dict__.update(args)

    def __getattr__(self, item):
        return getattr(self._object, item)

k = Korean()
b = British()

kor_adapter = Adapter(k, speak=k.speak_korean)
eng_adapter = Adapter(b, speak=b.speak_british)

print(eng_adapter.speak())
print(kor_adapter.speak())