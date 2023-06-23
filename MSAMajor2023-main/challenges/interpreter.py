expression = input("Expression: ")
parts = expression.split(" ")

num_1 = float(parts[0])
operator = parts[1]
num_2 = float(parts[2])

if operator == "+":
    answer = num_1 + num_2
elif operator == "-":
    answer = num_1 - num_2
elif operator == "*":
    answer = num_1 * num_2
elif operator == "/":
    answer = num_1 / num_2

print(f"{answer:.1f}")