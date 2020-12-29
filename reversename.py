name = input("Enter a name: ")
lizt = name.split(" ")
lizt.reverse()
for i in lizt:
	print(i.capitalize(), end= " ")
print()