import json


def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def count_multiples_of_4_with_key_2(data, key_name):
    count = 0
    total_groups = len(data) // 4
    missing_key_indices = []

    for i in range(total_groups):
        group = data[i * 4: (i + 1) * 4]
        if all(key_name in entry for entry in group):
            count += 1
        else:
            for j, entry in enumerate(group):
                if key_name not in entry:
                    missing_key_indices.append(i * 4 + j)

    # Save missing key indices to a file
    with open("/home/wtegge2/LLM4Decompile/AnghaBench/missing_key_indices.txt", "w") as file:
        for index in missing_key_indices:
            file.write(f"{index}\n")

    return count



json_file_path = "/home/wtegge2/LLM4Decompile/AnghaBench/angha-data-final.json"
data = load_data(json_file_path)
print(type(data))
print(len(data))
# print(type(data[0]))

# count_3 = count_multiples_of_4_with_key_2(data, "input_asm_prompt")
# print(count_3)