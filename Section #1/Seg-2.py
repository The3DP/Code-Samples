class PluginMeta(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        if name != "BasePlugin":
            PluginMeta.registry[name] = new_class
        return new_class

class BasePlugin(metaclass=PluginMeta):
    pass

class PluginA(BasePlugin):
    pass

class PluginB(BasePlugin):
    pass

print("Registered plugins:", PluginMeta.registry)
