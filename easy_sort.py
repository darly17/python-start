list_=[['Adam,',29],['Ricky',25],['Kessy',21]]

def s(x):
    return x[0]


r=sorted(list_,key=s)
print(r)
