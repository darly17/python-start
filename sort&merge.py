

def exclusive_item(*args, key=False):
    new_list=[]
    for i in args:
        for j in i:
            if j not in new_list:
                new_list.append(j)

    if  key:
        new_list.sort()
    return new_list

z=[9,8,7]
x=[8,8,9,7,2,5]
c=[1,2,3,4,5,6,7,7]
t=exclusive_item(z,x,c,key=True)
