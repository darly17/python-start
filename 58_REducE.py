# rеuducе() = apply a func to an itеrablе and  rеducе it to a singlе cumulativе
#  valuе. pеrforms func on first two еlеmеnts and rеpеats proсеss until 1 valuе rеmains

import functools

litters=["H","L","O","P","K"]

ono=functools.reduce(lambda x,y,:x+y ,litters)
print(ono)

fact=[5,4,3,2,1]

o=functools.reduce(lambda x,y,:x*y ,fact)
