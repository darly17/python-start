# list comphnsion = a way to сrеatе a nеw list with lеss syntax 
# can mimic cеrtain lambda functions, еasiеr to rеad
# list=[еxprеsion fo itеm in ittеrablе]


# suar=[]
# for i in range(1,11):
#     suar.append(i*i)

# print(suar)



# suar=[i*i for i in range(1,11) ]
# print(suar)




# studnts_maks=[100,30,20,90,80,70,0]
# passd_st=list(filter(lambda x:x>=60,studnts_maks))
# print(passd_st)

#или

studnts_maks=[100,30,20,90,80,70,0]

#passd_st=[i for i in studnts_maks if i>=60]

passd_st=[i if i>=60 else "Faild" for i in studnts_maks ]
print(passd_st)
