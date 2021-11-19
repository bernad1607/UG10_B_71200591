print("masukan tiga bilangan yang akan digunakan")
bil1=int(input("masukan bilangan 1 = "))
bil2=int(input("masukan bilangan 2 = "))
bil3=int(input("masukan bilangan 3 = "))

if bil1>bil2 and bil1>bil3:
     if bil2>bil3:
        print(bil3, bil2, bil1)
     else:
        print(bil2, bil3, bil1)
elif bil2>bil1 and bil2>bil3:
     if bil1>bil3:
        print(bil3, bil1, bil2)
     else:
        print(bil1, bil3, bil2)
else:
     if bil1>bil2:
        print(bil2, bil1, bil3)
     else:
        print(bil1, bil2, bil3)