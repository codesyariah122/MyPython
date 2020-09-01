# angka1 = 0
# string = ""

# while angka1 <= 5:
# 	angka2 = angka1

# 	while angka2 > 0:
# 		string = string + "*"
# 		angka2 = angka2 - 1

# 	string = string + "\n"
# 	angka1 = angka1 + 1

# print(string)

# angka1 = 5
# string = ""

# while angka1 > 0:
# 	angka2 = angka1

# 	while angka2 > 0:
# 		string = string + "*"
# 		angka2 = angka2 - 1

# 	string = string + "\n"
# 	angka1 = angka1 - 1

# print(string)

def triangle():
	x = int(input('X : ? '))
	y = int(input('y : ? '))
	string = ""

	while x > 0:
		y = x

		while y > 0:
			string = string + "*"
			y = y - 1

		string = string + "\n"
		x = x - 1
	print(string)

triangle()