from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

print("📦 Loading CodeGemma model...")

model_name = "google/codegemma-2b"
#hf_token = "your_hf_token_here"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create pipeline
llm = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=False
)

def analyze_code_with_gemma(code: str) -> str:
    """
    Sends Java code to CodeGemma and returns AI explanation.
    """
    prompt = f"""You are an expert reverse engineer and deobfuscator.
Analyze the following Java code and explain what it does.
Also, suggest better variable, class, or method names if applicable.

Java Code:
{code}
"""
    result = llm(prompt)
    return result[0]['generated_text']