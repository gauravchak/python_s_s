def getmax(x):
    y = x[0]
    for num in x:
        if num > y:
            y = num
    return y
