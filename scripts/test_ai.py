from utility import collect_java_files, read_file
from ai_model import analyze_code_with_gemma
from output_writer import save_output

SOURCE_DIR = "./decompiled/sources"
OUTPUT_DIR = "./ai_output"

files = collect_java_files(SOURCE_DIR)

if files:
    file_path = files[0]
    java_code = read_file(file_path)

    print(f"📄 Analyzing: {file_path}")
    snippet = '\n'.join(java_code.splitlines()[:300])

    ai_response = analyze_code_with_gemma(snippet)

    save_output(file_path, java_code, ai_response, OUTPUT_DIR)
else:
    print("❌ No Java files found.")