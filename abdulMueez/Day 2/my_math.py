#int1 = 5
#int2 = 2

def calculate(method, int1, int2):
    method = method.lower()
    if ( method == "add"):
        return (int1+int2)
    elif (method == "subtract"):
        return (int1-int2)
    elif (method == "multiply"):
        return (int1*int2)
    elif (method == "divide"):
        return(int1/int2)
    else : 
       return(print("method not available"))
