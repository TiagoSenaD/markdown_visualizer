from pathlib import Path

class MarkdownReader:
    @staticmethod
    def get_md_files(directory):
        if not Path(directory).exists() or not Path(directory).is_dir():
            return []
        return sorted([f for f in Path(directory).iterdir() if f.is_file() and f.suffix == '.md'])

    @staticmethod
    def read_file(directory, filename):
        path = Path(directory) / filename
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()