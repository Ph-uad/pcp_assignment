def load_dataset_module(file):
    cleaned_data = []
    keys = []

    with open(file, 'r') as file:
        keys = file.readline().rstrip('\n').split(',')
        
        for line in file:        
            values = []
            current_value = ''
            inside_quotes = False
            observation = line.rstrip('\n')

            for char in observation:
                if char == '"':
                    inside_quotes = not inside_quotes 
                elif char == ',' and not inside_quotes:
                    values.append(current_value)
                    current_value = ''
                else: 
                    current_value += char

            if current_value:
                values.append(current_value)

            cleaned_data.append(dict(zip(keys, values)))

    return cleaned_data