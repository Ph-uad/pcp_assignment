def statistics_module(arr, parameter, options):
    
    data = []
    # createw a list from the data of parameter in the array
    for obj in arr:
         data.append(eval(obj[parameter.lowwer()]))
    
    if(options =='minimum_value' or options.lower() == 'minimum value' or options == 2):
        return min(data)
    elif(options =='maximum_value ' or options.lower() == 'maximum value' or options == 4  or options.lower() == 'max'  or options.lower() == 'max value'):
        return max(data)
    elif(options =='average' or options.lower() == 'average value' or options == 3  or options.lower() == 'mean'  or options.lower() == 'mean value'):
        return sum(data) / len(data)
    elif(options =='mode' or options.lower() == 'mode value' or options == 1  or options.lower() == 'mode'  or options.lower() == 'most frequent'  or options):
        numbers = {}
        
        for num in data:
            if not num in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
            
        result = [n for n,m in numbers.items() if m == max(numbers.values())]
        freq = numbers[result[0]]
        
        return (result[0], freq)
    elif(options =='variance' or options.lower() == 'variance value' or options == 5  or options.lower() == 'variance'  or options.lower() == 'dispersion' ):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return variance
    elif(options =='standard_deviation' or options.lower() == 'standard deviation value' or options == 6  or options.lower() =='standard deviation'  or options.lower() == 'deviation' ):
        return variance(data) ** 0.5
    else:
        return 'Invalid option'