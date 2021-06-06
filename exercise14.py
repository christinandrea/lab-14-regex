#Christina Andrea Putri - Universitas Kristen Duta Wacana
import re

#Anna adalah mahasiswi ingin mencari data menggunakan e-mail yang diberikan kampus. Jika ditemukan, maka data akan berupa nama, jurusan, dan universitas.

#Input : email
#Proses : regex memecah sesuai dengan formatnya, lalu akan diformat kembali menggunakan fitur split
#Output : mengeluarkan nama, jurusan, dan universitas

def findData(n):

    mt = re.findall("[A-Za-z]\w+.\w+",n)

    spl1 = mt[0].split(".")
    spl2 = mt[1].split(".")


    print("Nama: ", end="")
    for i in spl1:
        print(i, end=" ")
    print("\n")
    if spl2[0]=="ti":
        print("Jurusan : Informatika")
    elif spl2[0]=="si":
        print("Jurusan : Sistem Informasi")
    else:
        print("Bukan Fakultas Teknologi Informasi.")
    if spl2[1]=="ukdw":
        print("Universitas : Universitas Kristen Duta Wacana")
    else:
        print("Bukan UKDW.")

try:
    print("Data Fakultas Teknologi Informasi")
    em = input("Email:  ")

    findData(em)

except:
    print("Terjadi kesalahan, silahkan coba lagi")