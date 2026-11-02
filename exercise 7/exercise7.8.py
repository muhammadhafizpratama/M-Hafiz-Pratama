sandwich_orders = ["tuna", "ham", "chicken", "veggie", "cheese"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")