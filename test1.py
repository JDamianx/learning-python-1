def adding(x):
    global var
    var = 7
    return x + var
 
 
print(adding(4)) # outputs: 11
print(var)