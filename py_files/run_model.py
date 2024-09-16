from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = 'arise-sustech/llm4decompile-1.3b'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path,torch_dtype=torch.bfloat16).cuda()


fileName = '/home/wtegge2/LLM4Decompile/test/test_O0.asm'
with open(fileName,'r') as f:
    asm_func = f.read()


inputs = tokenizer(asm_func, return_tensors="pt").to(model.device)
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=512)

c_func_decompile = tokenizer.decode(outputs[0][len(inputs[0]):-1])

# print into an output file
with open('/home/wtegge2/LLM4Decompile/output', 'w') as f:
    print(c_func_decompile, file=f)
