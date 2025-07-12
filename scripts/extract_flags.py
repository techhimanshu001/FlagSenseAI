import os
import json
import re

AI_OUTPUT_DIR = "./ai_output"

SUSPICIOUS_KEYWORDS = ["flag", "debug", "bypass", "unlock", "secret", "token", "phenotype"]

def extract_flags_from_code(code):
    """
    Extracts string literals from Java code and filters those with suspicious flag-like keywords.
    """
    matches = re.findall(r'"([^"]{5,50})"', code)  # find strings between quotes
    filtered = [
        m for m in matches
        if any(kw in m.lower() for kw in SUSPICIOUS_KEYWORDS)
        and not m.startswith("http")
    ]
    return filtered

def extract_all_flags(directory=AI_OUTPUT_DIR):
    all_flags = set()
    for file in os.listdir(directory):
        if file.endswith(".json"):
            full_path = os.path.join(directory, file)
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    code = data.get("original_code", "")
                    flags = extract_flags_from_code(code)
                    all_flags.update(flags)
            except Exception as e:
                print(f"❌ Error reading {file}: {e}")
    return sorted(all_flags)

if __name__ == "__main__":
    found_flags = extract_all_flags()
    print(f"\n✅ Extracted {len(found_flags)} potential flag strings:\n")
    for flag in found_flags:
        print(" -", flag)