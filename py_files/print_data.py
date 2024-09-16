import json

with open('/home/wtegge2/LLM4Decompile/decompile-eval/decompile-eval-copy.json', 'r') as json_file:
    data = json.load(json_file)

with open('/home/wtegge2/LLM4Decompile/out.c', 'w') as f:
    for item in data:
        if(item["type"] == "O0"):
            print(item["c_func"] + " ", file=f)
            os.system("gcc -c out.c")
            item["binary"] = merge_binary_lines('/home/wtegge2/LLM4Decompile/out.o', f)








