class LLMClient:
    """Unified interface for all LLM backends."""

    def generate(self, prompt: str) -> str:
        raise NotImplementedError
