from utility import collect_java_files, read_file

SOURCE_DIR = "./decompiled/sources"

# Collect Java files
files = collect_java_files(SOURCE_DIR)
print(f"✅ Found {len(files)} .java files")

# Read the first file as a test
if files:
    content = read_file(files[0])
    print(f"📄 File: {files[0]}")
    print(f"📦 Sample Content:\n{'-'*40}\n{content[:500]}...\n{'-'*40}")