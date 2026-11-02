sandwich_orders = ["tuna", "ham", "pastrami", "chicken",
                   "pastrami", "veggie", "pastrami", "cheese"]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")