# angka = 1

# while angka > 0 and angka < 11:
#     angka = int(input("Masukan bilangan bulat: "))
#     if angka >= 1:
#         print("Bilangan Positif")
#     elif angka < 0:
#         print ("Bilangan Negatif")
#     else:
#         print("Bilangan Nol")

while True:
    nama = input("Masukan nama Anda: ")

    if nama == "x":
        break
    elif nama =="Aldi":
        continue

    print("Selamat datang ",nama)