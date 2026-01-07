a = input("Enter first boolean value (true/false): ").lower() == "true"
b = input("Enter second boolean value (true/false): ").lower() == "true"

print("\nResults:")
print(f"a AND b = {a and b}")
print(f"a OR b  = {a or b}")
print(f"NOT a   = {not a}")
print(f"NOT b   = {not b}")
