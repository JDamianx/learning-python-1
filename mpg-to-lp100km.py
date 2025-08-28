# 1 mila amerykańska = 1609.344 metry=1,609344km;
# 1 galon amerykański = 3,785411784 litrów.

    # **********LOGIC l/100km to mpgalon*************************
    # 3,9l(quantity)/100km(distance)
    # x miles(distance)/galon(1)
    # 1 litr = x galon america
    # 1 km = x miles america
    # 1,609344 km = 1 mila
    # (1mila x 1km)/1,609344km=0,621371 mili
    # 0,621371 mili=1km
    # 1 km = 0,621371 miles america
    # 1litr = x galon 
    # 3,785411784 litr = 1 galon
    # (1litr*1galon)/3,785411784litr=0,2641720523581484 galon
    #100km=62,1371miles
    # 1litr = 0,2641720523581484 galon
    # 3,9 litr/100km
    # 3,9litr-x
    # 3,785411784 litr - 1gal
    # mile=km*0,621371
    # galony= litry/3,785411784

    # mpg=mile/galony
    # mpg =(62,1371)/(3,9/3,785411784)=60,31141296502214mpg
    # 3,9l/100km =60,3mpg
    # *********************END**********************************
    # *********LOGIC mpgalon to l/100km*************************
    #  change mile to 100km
    #  (mpg *1.609344)/100
    #  litre=3.785411784
    # 3.785411784/(mpgal*1.609344)/100
    # *********************END**********************************
    # 


def liters_100km_to_miles_gallon(liters):
    mpg=(62.1371)/(liters/3.785411784)
    return mpg
    
def miles_gallon_to_liters_100km(mpgal):
    kmpg=(mpgal*1.609344)
    gp100km=100/kmpg
    litres=3.785411784
    return gp100km*litres
    

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
