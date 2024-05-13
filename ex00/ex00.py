def conversion_miles_en_km():
     return distance_miles * 1.60934

distance_miles = float(input("Veuillez entrer la distance en miles : "))
distance_km =   conversion_miles_en_km()  
print(f"{distance_miles} miles équivaut à {distance_km} kilomètres.")
