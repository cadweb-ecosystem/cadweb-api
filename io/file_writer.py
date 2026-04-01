from pathlib import Path

class FileWriter:
    def write(self, path: str, content: str):
        p = Path(path)
        p.write_text(content)
        return True
