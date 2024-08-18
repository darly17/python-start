# dict comphnsion = сrеatе dict using an еxpеssion can rеplacе for loops and cеrtain lambda functions

# dict={kеy:еxprеssion for {kеy,valuе} in ittеrablе}

citiis_in_F={'NY':32,'Boston':75,'LA':100,'Chicago':50}


city_in_C={key:(round((value-32)*(5/9))) for (key ,value) in citiis_in_F.items()}

print(city_in_C)

forcast={'NY':"snoy",'Boston':"sunny",'LA':"cloudy",'Chicago':"sunny"}

sunny={key:value for (key ,value) in forcast.items() if value == "sunny"}

print(sunny)

cold={key: "hot"if value>60  else "cold" for (key ,value) in citiis_in_F.items()}

print(cold)
def chk_tmp(value):
    if value>60:
        return "hot"
    else:
        return "cold"
        


dsc_city={key: chk_tmp(value) for (key ,value) in citiis_in_F.items()}

print(dsc_city)