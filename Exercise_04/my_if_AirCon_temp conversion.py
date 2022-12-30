temp_var = [number * 15 for number in range(0,10)]


total_now = 0

for item in temp_var:
	total_now = item - 273
	print("In celcius ",item,"Kelvin would be : ",total_now, "Degrees")
	total_now = ((((item)-273.15)*1.8)+32)
	print("In Fareghight ",item,"Kelvin would be : ",total_now, "Degrees")