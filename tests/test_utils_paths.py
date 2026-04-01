from cadweb_api.utils.paths import project_root
from pathlib import Path

def test_project_root_is_directory():
    root = project_root()
    assert isinstance(root, Path)
    assert root.exists()
