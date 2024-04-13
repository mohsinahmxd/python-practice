# dictionary - a changeable, unordered collection of unique key value pairs - it's also fast because it uses hashing allowing access of a value quickly

capitals = {
    "UK" : "London",
    "France" : "Paris",
    "Russia" : "Moscow"
}

#access values using the key, rather than the index
print(capitals.get("UK")) # use the get method on dictionaries rather than square brackets as it's safer ie you will get "None" rather than an error if that key value does not exist in the dictionary

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

# The .items() method in Python dictionaries returns a view object that provides a dynamic view of the dictionary’s key-value pairs. This view object behaves like a set of tuples, where each tuple contains a key-value pair from the dictionary.

# When you use the .items() method in a for loop, Python iterates over this view object, retrieving one tuple at a time. Each tuple consists of two elements: the key and its corresponding value from the dictionary.

capitals.update({"Germany": "Berlin"})
capitals.update({"UK":"Bradford"})

for key, value in capitals.items():
    print(key, value)