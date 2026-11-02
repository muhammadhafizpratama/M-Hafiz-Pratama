# Daftar tempat yang ingin dikunjungi
places = ["Tokyo", "Paris", "Bali", "London", "Seoul"]

print("Original list:")
print(places)

print("\nAlphabetical order (sorted):")
print(sorted(places))

print("\nOriginal list after sorted:")
print(places)

print("\nReverse alphabetical order (sorted):")
print(sorted(places, reverse=True))

print("\nOriginal list after reverse sorted:")
print(places)

places.reverse()
print("\nList after reverse:")
print(places)

places.reverse()
print("\nList back to original order:")
print(places)

places.sort()
print("\nList after sort(alphabetical):")
print(places)

places.sort(reverse=True)
print("\nList after sort(reverse alphabetical):")
print(places)