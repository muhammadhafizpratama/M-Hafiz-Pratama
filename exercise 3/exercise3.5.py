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