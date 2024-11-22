def merge_inputs(input1:list, input2:list)->list:
    input1.extend(input2)
    final = sorted(input1)
    return final
