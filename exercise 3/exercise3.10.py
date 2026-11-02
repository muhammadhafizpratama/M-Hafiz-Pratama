negara = ["Indonesia", "Jepang", "Australia", "Kanada", "Brazil"]

print("List awal:", negara)

negara.append("India")
print("Setelah append:", negara)

negara.insert(1, "Malaysia")
print("Setelah insert:", negara)

negara.remove("Australia")
print("Setelah remove:", negara)

data_hapus = negara.pop(2)
print("Data yang di-pop:", data_hapus)
print("Setelah pop:", negara)

negara.append("India")
print("Jumlah 'India':", negara.count("India"))

print("Jumlah elemen list:", len(negara))

negara.sort()
print("Setelah sort:", negara)

negara.reverse()
print("Setelah reverse:", negara)

print("\nDaftar Negara:")
for n in negara:
    print("-", n)