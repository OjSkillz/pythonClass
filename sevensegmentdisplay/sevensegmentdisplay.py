display = [[' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ']
           ]

def display_output_for(display_code):

    if len(display_code) != 8:
        raise ValueError('Invalid code: display code must be eight digits long')

    elif display_code[-1::] != "0":

        if [not character.isdigit() for character in display_code].__contains__(True):
            raise TypeError('Invalid code: display code cannot contain letters or special characters')

        elif [int(character) > 1 for character in display_code].__contains__(True):
            raise ValueError('Invalid code: display code can only contain 0s and 1s')

        modify_segment_a_with(display_code)
        modify_segment_b_with(display_code)
        modify_segment_c_with(display_code)
        modify_segment_d_with(display_code)
        modify_segment_e_with(display_code)
        modify_segment_f_with(display_code)
        modify_segment_g_with(display_code)

    output = "\n"
    for count in range(len(display)):
        output += f"{''.join(display[count])}\n"
    return output

def modify_segment_a_with(display_code):
    activation_codes = list(display_code[:len(display_code) - 1:])

    if activation_codes[0] == "1":
        for count in range(len(display[0])):
            display[0][count] = "#"

def modify_segment_b_with(display_code):
    activation_codes = list(display_code[:len(display_code) - 1:])
    if activation_codes[1] == "1" :
        display[1][len(display[1]) - 1] = "#" ; display[2][len(display[2]) - 1] = "#"

def modify_segment_c_with(display_code):
    activation_codes = list(display_code[:len(display_code) - 1:])
    if activation_codes[2] == "1" :
        display[4][len(display[4]) - 1] = "#" ; display[5][len(display[5]) - 1] = "#"

def modify_segment_d_with(display_code):
    activation_codes = list(display_code[:len(display_code) - 1:])
    if activation_codes[3] == "1" :
        for count in range(len(display[6])):
            display[6][count]= "#"

def modify_segment_e_with(display_code):
    activation_codes = list(display_code[:len(display_code) - 1:])
    if activation_codes[4] == "1" :
        display[5][0] = "#" ; display[4][0] = "#"

def modify_segment_f_with(display_code):
    activation_codes = list(display_code[:len(display_code) - 1:])
    if activation_codes[5] == "1":
        display[2][0] = "#";
        display[1][0] = "#"

def modify_segment_g_with(display_code):
    activation_codes = list(display_code[:len(display_code) - 1:])
    if activation_codes[6] == "1" :
        for count in range(len(display[3])):
            display[3][count] = "#"