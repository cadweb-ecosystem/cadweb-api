import pytest
from cadweb_api.agent.base_agent import BaseAgent

def test_base_agent_requires_run():
    agent = BaseAgent()
    with pytest.raises(NotImplementedError):
        agent.run("test")
