def merge_inputs_alternatingly(input1:list, input2:list)->list:
    merged_list = []
    merged_list.extend(input1)
    for index in range(1, (len(input1) + len(input2)), 2):
        merged_list.insert(index, input2.pop(0))
    return merged_list
