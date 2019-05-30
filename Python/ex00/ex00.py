from __future__ import print_function
a = raw_input("write string: ")
for i in a:
	if i == " " or i == "\t" or i == "\n":
		i = ""
	print(i, end = '')
print()
