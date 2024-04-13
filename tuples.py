# tuples are a collection, similar to lists as they are ordered aka they remain in the order they are placed and are indexed

# howeever they are unchangeable aka immutable once createed - used to group together related data

student = ("John", 21, "male") # use normal brackets instead of square ones for tuples

print(student.count("male"))
print(student.index("John"))

for item in student:
    print(item)

if "John" in student:
    print("Bro is here")

