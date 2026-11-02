fav_num = {
    'Alisya': [8, 13],
    'Bobi': [43, 16],
    'Charli': [14, 23],
    'Diana': [6, 82],
    'Eva': [24, 2]
}
for name, numbers in fav_num.items():
    print(f"{name}.")
    for number in numbers:
        print(f"  - {number}.")