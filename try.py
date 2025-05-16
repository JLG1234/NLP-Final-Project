from mlx_lm import load, generate
from analyze import labels

model, tokenizer = load(path_or_hf_repo="./models/Ministral-3b-instruct", adapter_path="./adapters")

prompt = input("Enter your prompt: ")

messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True
)

# Set temp=0 for deterministic output
text = generate(model, tokenizer, prompt=prompt, verbose=False)

if text in labels:
    print(f"Label: {text}")
else:
    print("result:", text)
    print("Label not found in the predefined labels.")