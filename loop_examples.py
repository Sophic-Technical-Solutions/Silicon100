# Python Loop Examples

# --- for loop over a list ---
print("=== for loop over a list ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# --- for loop with range ---
print("\n=== for loop with range ===")
for i in range(1, 6):
    print(f"  i = {i}")

# --- while loop ---
print("\n=== while loop ===")
count = 0
while count < 5:
    print(f"  count = {count}")
    count += 1

# --- break ---
print("\n=== break ===")
for n in range(10):
    if n == 4:
        print(f"  Breaking at n = {n}")
        break
    print(f"  n = {n}")

# --- continue ---
print("\n=== continue (skip evens) ===")
for n in range(6):
    if n % 2 == 0:
        continue
    print(f"  n = {n}")
