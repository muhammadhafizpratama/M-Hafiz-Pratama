people = [
    {'first_name': 'muhammad', 'last_name': 'hafiz', 'age': '19', 'city': 'pekalongan'},
    {'first_name': 'hafiz', 'last_name': 'pratama', 'age': '19', 'city': 'pekalongan'},
    {'first_name': 'pratama', 'last_name': 'hafiz', 'age': '19', 'city': 'pekalongan'}
]
for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()}, Age: {person['age']}, City: {person['city'].title()}")
