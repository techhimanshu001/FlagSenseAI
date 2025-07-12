import os
from utility import collect_java_files, read_file
from ai_model import analyze_code_with_gemma
from output_writer import save_output
from time import sleep

SOURCE_DIR = "./decompiled/sources"
OUTPUT_DIR = "./ai_output"

def is_already_processed(file_path):
    base_name = os.path.basename(file_path).replace(".java", "")
    json_path = os.path.join(OUTPUT_DIR, f"{base_name}.json")
    return os.path.exists(json_path)

def main():
    files = collect_java_files(SOURCE_DIR)
    total = len(files)
    
    print(f"\n🔍 Total Java files found: {total}\n")

    for idx, file_path in enumerate(files):
        base_name = os.path.basename(file_path)

        if is_already_processed(file_path):
            print(f"[{idx+1}/{total}] ⏩ Skipping already processed: {base_name}")
            continue

        code = read_file(file_path)
        if not code:
            print(f"[{idx+1}/{total}] ❌ Failed to read: {base_name}")
            continue

        # Optional: Skip huge files
        if len(code) > 20000:
            print(f"[{idx+1}/{total}] ⚠ Skipping large file: {base_name}")
            continue

        snippet = '\n'.join(code.splitlines()[:300])  # first 300 lines
        print(f"[{idx+1}/{total}] 🤖 Processing: {base_name} ...")

        try:
            ai_result = analyze_code_with_gemma(snippet)
            save_output(file_path, code, ai_result, OUTPUT_DIR)
        except Exception as e:
            print(f"❌ Error processing {base_name}: {e}")
            sleep(1)

    print("\n✅ Batch processing complete.")

if __name__ == "__main__":
    main()