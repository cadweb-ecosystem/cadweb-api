from cadweb_api.tools.tool_registry import ToolRegistry
from cadweb_api.tools.tool_base import ToolBase

class DummyTool(ToolBase):
    def run(self):
        return "ok"

def test_tool_registry_register_and_get():
    ToolRegistry.register("dummy", DummyTool())
    tool = ToolRegistry.get("dummy")
    assert tool is not None
    assert tool.run() == "ok"
