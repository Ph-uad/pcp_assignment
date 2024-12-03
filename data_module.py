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



def statistics_module(arr, parameter, options):
    
    data = []
    
    for obj in arr:
         data.append(eval(obj[parameter]))
    
    if(options =='minimum_value'):
        return min(data)
    elif(options =='maximum_value'):
        return max(data)
    elif(options =='average'):
        return sum(data) / len(data)
    elif(options =='mode'):
        numbers = {}
        
        for num in data:
            if not num in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
            
        result = [n for n,m in numbers.items() if m == max(numbers.values())]
        freq = numbers[result[0]]
        
        return (result[0], freq)
    elif(options =='variance'):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return variance
    elif(options =='standard_deviation'):
        return variance(data) ** 0.5
    else:
        return 'Invalid option'
    
    
    
    

