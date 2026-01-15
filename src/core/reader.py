import os

class MarkdownReader:
    @staticmethod
    def get_md_files(directory):
        if not os.path.exists(directory) or not os.path.isdir(directory):
            return []
        return sorted([f for f in os.listdir(directory) if f.endswith('.md')])

    @staticmethod
    def read_file(directory, filename):
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()