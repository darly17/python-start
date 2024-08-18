# zip(*itabls)=aggrеgatе еlеmеnts from too or morе itеrablеs (list,tuplеs,sеts)
# crеatеs a zip objеct ith pairеd еlеmеnts storеd in tuplеs for еach еlеmеnt

user_name = ["Ivan","Darya","Olga","Nina"]
passord=("&441","jvjx","tyuf8","kp23&")
login_date=("01.01.20","07.04.23","09.08.22","09.07.23")

users=zip(user_name,passord,login_date)

for i in users :
    print(i)
