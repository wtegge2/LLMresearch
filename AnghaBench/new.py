import json

def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


# use this function to print out the 4 key-value pairs in the dictionary
def new_func(filename):

    with open(filename, 'r') as json_file:
        json_list = list(json_file)

    counter = 0
    for json_str in json_list:
        
        item = json.loads(json_str)
        if counter == 2:
            #print(type(item))
            #print(item.keys())
            #exit()
            print("Name: " + "\n")
            print(item["name"])
            print("\n")
            print("Input: " + "\n")
            print(item["input"])
            print("\n")
            print("Input_ori: " + "\n")
            print(item["input_ori"])
            print("\n")
            print("Output: " + "\n")
            print(item["output"])
            break
        counter = counter + 1

# use this function to access the output dictionary within each dictionary
def get_output_entry(filename):
    with open(filename, 'r') as json_file:
        json_list = list(json_file)

    counter = 0
    for json_str in json_list:
        item = json.loads(json_str)
        if counter == 2:
            output_ = item["output"]
            print("opt-state-O0" + "\n" + output_["opt-state-O0"] + "\n")
            print("opt-state-O1" + "\n" + output_["opt-state-O1"] + "\n")
            print("opt-state-O2" + "\n" + output_["opt-state-O2"] + "\n")
            print("opt-state-O3" + "\n" + output_["opt-state-O3"] + "\n")
            break
        counter = counter + 1


json_path = "/home/wtegge2/LLM4Decompile/train/AnghaBench_compile.jsonl"
# file = "/home/wtegge2/LLM4Decompile/AnghaBench/temp.txt"
# new_func(json_path) 
get_output_entry(json_path)




# example of what the output entry looks like
# output = {
#     "opt-state-O0" = "assembly code of optimization O0",
#     "opt-state-O1" = "assembly code of optimization O1",
#     "opt-state-O2" = "assembly code of optimization O2",
#     "opt-state-O3" = "assembly code of optimization O3"
# }
