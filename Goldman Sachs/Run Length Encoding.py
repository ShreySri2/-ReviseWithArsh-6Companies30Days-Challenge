def encode(arr):
    # Code here
    prev = arr[0]
    count = 0
    
    res = []
    for char in arr:
        if char == prev:
            count+=1
        else:
            res.append(prev + str(count))
            count = 1
            prev = char
    res.append(prev + str(count))      
    return ''.join(res)