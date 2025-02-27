def modify_string(string, modifier):
        if len(string) % 2 == 0:
            return modifier.join([string[:len(string) // 2], string[len(string) // 2:]])
        else:
            string += modifier
            return string