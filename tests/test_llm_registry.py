from cadweb_api.llm.llm_registry import LLMRegistry
from cadweb_api.llm.llm_client import LLMClient

class DummyLLM(LLMClient):
    def generate(self, prompt: str) -> str:
        return "response"

def test_llm_registry_register_and_get():
    LLMRegistry.register("dummy", DummyLLM())
    client = LLMRegistry.get("dummy")
    assert client is not None
    assert client.generate("hi") == "response"
