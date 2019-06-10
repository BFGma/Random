a = input("write string: ")
for i in a:
	if i == " " or i == "\t" or i == "\n":
		i = ""
	print(i, end = '')
print()
