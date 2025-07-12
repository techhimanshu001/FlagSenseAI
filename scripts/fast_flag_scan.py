import os
import re
from utility import collect_java_files, read_file
from ai_model import analyze_code_with_gemma
from output_writer import save_output

SOURCE_DIR = "./decompiled/sources"
OUTPUT_DIR = "./ai_output_fast"
os.makedirs(OUTPUT_DIR, exist_ok=True)

KEYWORDS = ["flag", "debug", "qr", "bypass", "secret", "unlock", "phenotype", "mode"]

def contains_keywords(code):
    """Check if the code has at least one relevant keyword"""
    for word in KEYWORDS:
        if word.lower() in code.lower():
            return True
    return False

def main():
    files = collect_java_files(SOURCE_DIR)
    print(f"\n🔍 Total Java files: {len(files)}")

    filtered = []
    for f in files:
        code = read_file(f)
        if contains_keywords(code):
            filtered.append((f, code))

    print(f"⚡ Shortlisted {len(filtered)} suspicious files for AI scan\n")

    for i, (file_path, code) in enumerate(filtered):
        base = os.path.basename(file_path)
        print(f"[{i+1}/{len(filtered)}] 🤖 Analyzing: {base}")
        snippet = '\n'.join(code.splitlines()[:500])  # Give more code context

        try:
            ai_result = analyze_code_with_gemma(snippet)
            save_output(file_path, code, ai_result, OUTPUT_DIR)
        except Exception as e:
            print(f"❌ Error analyzing {base}: {e}")

    print("\n✅ Fast flag scan complete.")

if __name__ == "__main__":
    main()