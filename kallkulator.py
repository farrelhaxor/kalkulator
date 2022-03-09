author = ("author = farrel")
print(author)
Team = ("Team = Malang Xploit")
print(Team)


operasi = input("tentukan operasi yang ingin anda lakukan, misal nya +,-,*,/: ")

x = int(input("masukan angka pertama anda :"))
y = int(input("masukan angka kedua anda :"))

if operasi == "+" :
	print("hasil dari ",x,"+",y,"=",x+y)
elif operasi == "-":
	print ("hasil dari",x,"-",y,"=",x-y)
elif operasi == "*":
    print ("hasil dari",x,"*",y,"=",x*y)
elif operasi == "/":
	print ("hasil dari",x,"/",y,"=",x/y)
	
