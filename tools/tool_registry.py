class ToolRegistry:
    _tools = {}

    @classmethod
    def register(cls, name, tool):
        cls._tools[name] = tool

    @classmethod
    def get(cls, name):
        return cls._tools.get(name)
