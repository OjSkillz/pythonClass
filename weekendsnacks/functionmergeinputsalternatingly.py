def merge_inputs_alternatingly(input1:list, input2:list)->list:
    merged_list = []
    for index in range(0, len(input1) + len(input2), 2): 
        for index2 in range(len(input1)):
            merged_list[index2] = input1[index2]
    return merged_list
