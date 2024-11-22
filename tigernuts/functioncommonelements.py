def check_common(list_1, list_2):
    common = []
    for element in list_1:
        if element in list_2:
            common.append(element)
    return common
        
