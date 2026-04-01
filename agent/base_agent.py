class BaseAgent:
    """Abstract agent interface."""

    def run(self, task: str):
        raise NotImplementedError("Agents must implement run()")
