import json

# Replace 'your_file.jsonl' with the path to your JSONL file
file_path = '/home/wtegge2/LLM4Decompile/decompile-eval/decompile-eval-copy.json'

# Open the file in read mode
f = open(file_path) 
data = json.load(f)
f.close()
print(data)
exit()

with open(file_path, 'r') as file:
    for line in file:
        # Parse each line as a JSON object
        print(line)
        exit()
        json_object = json.loads(line)
        
        # Check if 'code_tokens' key exists and process it
        if 'c_func' in json_object:
            code_sentence = ' '.join(json_object['c_func'])
            print("Code Tokens as a Sentence:")
            print(code_sentence)
        
        # Check if 'doc_string_tokens' key exists and process it
        if 'c_test' in json_object:
            doc_sentence = ' '.join(json_object['c_test'])
            print("Doc String Tokens as a Sentence:")
            print(doc_sentence)
        
        print("--------------------------------------------------")
        exit()