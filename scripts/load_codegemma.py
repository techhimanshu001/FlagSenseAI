from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login

# Model name (2B parameter size)
#   # Replace with your Hugging Face token
model_name = "google/codegemma-2b"

print("📦 Loading tokenizer and model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Setup inference pipeline
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Test prompt
prompt = """Explain the purpose of the following Java method:

public void checkFlag(String input) {
    if (input.equals("debug_bypass_phenotype")) {
        unlockSecretMode();
    }
}"""

print("🧠 Generating explanation...")
response = llm_pipeline(prompt, max_new_tokens=100, do_sample=False)[0]['generated_text']
print(response)