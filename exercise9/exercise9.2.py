class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurant1 = Restaurant("Warung Indomie", "Indonesian Food")
restaurant2 = Restaurant("Pizza Hut", "Italian Food")
restaurant3 = Restaurant("Sushi Tei", "Japanese Food")

restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()