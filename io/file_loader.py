from pathlib import Path

class FileLoader:
    def load(self, path: str):
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(path)
        return p.read_text()
