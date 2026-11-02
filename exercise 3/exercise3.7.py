list = ["jacobi", "ironi", "rusdi"]
message = f" please come to my dinner tonight, {list[0]}"
message += f" \nplease come to my dinner tonight, {list[1]}"
message += f" \nplease come to my dinner tonight, {list[2]}"
print(message)

message = f"{list[1]} cant come to my dinner tonight"
print(message)
list.remove("ironi")
list.insert(3, "gatot")
message = f" please come to my dinner tonight, {list[0]}"
message += f" \nplease come to my dinner tonight, {list[1]}"
message += f" \nplease come to my dinner tonight, {list[2]}"
print(message)

message = "i just found a bigger dinner table, so i am inviting more guests"
list.insert(3, "riski")
list.insert(4, "bagas")
list.append("rehan")
print(f" {message}, {list[3]}")
print(f" {message}, {list[4]}")
print(f" {message}, {list[5]}")

message = "sorry for this information, but i can only invite two people for dinner"
while len(list) > 2:
	popped_guest = list.pop()
	print(f" {message}: {popped_guest}")
message = f"you are still invited to my dinner tonight, {list[0]}"
message += f" \nyou are still invited to my dinner tonight, {list[1]}"
print(message)

print(f"\nNumber of guests invited to dinner: {len(list)}")