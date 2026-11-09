class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        print("User Information:")
        print(f"Name : {self.first_name} {self.last_name}")
        print(f"Age  : {self.age}")
        print(f"City : {self.city}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")


# Create several user instances
user1 = User("Gatot", "Doe", 25, "New York", "gatot@example.com")
user2 = User("Rusdi", "Smith", 30, "London", "rusdi@example.com")
user3 = User("Fuad", "Brown", 22, "Sydney", "fuad@example.com")

# Call methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()