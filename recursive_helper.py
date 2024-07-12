# illustrate recursive dictionaries
d = {}
d[1] = "one"
d[2] = d
str1 = "d[2]"

depth_found = 1
while True:
	str1 += "[2]"
	eval(str1)
	print(f"Found depth - {depth_found}")
	depth_found += 1
