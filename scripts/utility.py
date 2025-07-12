import os

def collect_java_files(source_dir: str):
    """
    Recursively collects all .java file paths from the given directory.
    """
    java_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".java"):
                full_path = os.path.join(root, file)
                java_files.append(full_path)
    return java_files


def read_file(filepath: str):
    """
    Reads the content of a Java file safely with error handling.
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read()
    except Exception as e:
        print(f"❌ Error reading file {filepath}: {e}")
        return None