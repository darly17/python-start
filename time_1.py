import time

print(time.ctime(0)) 
# convert a time expressed in seconds since epoch to a readable string

print(time.time()) #current sconds since epoch

print(time.ctime(time.time()))

time_obj=time.localtime()
print(time_obj)
print(local:=time.strftime("%B %d %Y %H:%M:%S",time_obj))


# tim_st="20 Apil, 2023"
# print(t_ob:= time.strptime(tim_st,"%d %B, %Y"))


tim_tupl=(2022,4,20,4,20,0,1,0,0)

time_st=time.asctime(tim_tupl)
print(time_st)


