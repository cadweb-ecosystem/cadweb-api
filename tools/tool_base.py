class ToolBase:
    """Base class for all cadweb tools."""

    def run(self, *args, **kwargs):
        raise NotImplementedError
