class Workflow:
    """Simple workflow container."""

    def __init__(self, steps=None):
        self.steps = steps or []

    def execute(self, context):
        for step in self.steps:
            context = step(context)
        return context
