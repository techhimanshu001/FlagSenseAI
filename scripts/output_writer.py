import os
import json

def save_output(code_path, original_code, ai_output, output_dir="./ai_output"):
    """
    Saves AI-generated explanations in both JSON and annotated Java text formats.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Safe filename
    base_name = os.path.basename(code_path).replace(".java", "")

    # 1. Save JSON
    data = {
        "file": code_path,
        "original_code": original_code,
        "ai_explanation": ai_output
    }

    json_path = os.path.join(output_dir, f"{base_name}.json")
    with open(json_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    # 2. Save Annotated Text
    annotated = f"// === AI Explanation Start ===\n// {ai_output.replace('\n', '\n// ')}\n// === AI Explanation End ===\n\n{original_code}"

    annotated_path = os.path.join(output_dir, f"{base_name}.java.txt")
    with open(annotated_path, "w", encoding='utf-8') as f:
        f.write(annotated)

    print(f"✅ Saved: {json_path}, {annotated_path}")