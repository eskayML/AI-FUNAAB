


def find_hcf(*args):
    ''' finds the hcf of any amount of arguments
    
    
    By Eskay🔥🔥
      '''
    ofl = []
    
    for i in args:
        ifl = []
        for x in range(1,i+1):
            if i%x == 0:
                ifl.append(x)
        ofl.append(ifl)
    
    flattened = [x for x in ofl for x in x]
    final_arr = []
    for num in flattened:
        if flattened.count(num)==len(args):
            final_arr.append(num)
    return max(final_arr)
            
           


result = find_hcf(10,25,50)

print(result)

    