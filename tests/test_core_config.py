from cadweb_api.core.config import Config

def test_config_paths_exist():
    Config.ensure_directories()
    assert Config.DATA.exists()
    assert Config.LOGS.exists()
