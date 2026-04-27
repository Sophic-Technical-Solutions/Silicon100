"""
Python Basic Data Structures Demo
"""

# ── Lists ──────────────────────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")
print("List:", fruits)
print("  Slice [1:3]:", fruits[1:3])
print("  Length:", len(fruits))

# ── Dictionaries ───────────────────────────────────────────────────────────────
person = {"name": "Alice", "age": 30, "city": "Boston"}
person["email"] = "alice@example.com"
person["age"] = 31
print("\nDict:", person)
print("  Keys:", list(person.keys()))
print("  Get with default:", person.get("phone", "N/A"))

# ── Sets ───────────────────────────────────────────────────────────────────────
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("\nSet A:", a)
print("  Union:", a | b)
print("  Intersection:", a & b)
print("  Difference A-B:", a - b)
a.add(9)
a.discard(1)
print("  After add(9) / discard(1):", a)

# ── Arrays (via array module) ──────────────────────────────────────────────────
import array
int_array = array.array("i", [10, 20, 30, 40, 50])
int_array.append(60)
print("\narray.array:", int_array)
print("  Typecode:", int_array.typecode, "| Count:", len(int_array))

# ── Summary ────────────────────────────────────────────────────────────────────
print("\n── Structure Summary ──")
structures = {
    "list":        "ordered, mutable, allows duplicates",
    "dict":        "key-value pairs, mutable, unique keys",
    "set":         "unordered, mutable, unique elements",
    "array":       "typed, compact, mutable sequence"
}
for name, desc in structures.items():
    print(f"  {name:<14} {desc}")
