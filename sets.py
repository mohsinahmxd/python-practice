# a set is a collection of unordered, unindexed however UNIQUE only values
# you can add dupes to the set but the dupes will be removed when you run the code
# you can add, remove and clear from a set - use setup.add, etc
# you can do setup.update(name of another set) and add all the items from this other set to setup and vice versa
# you can also make a whole new set from 2 other sets, use newset = setup.union(anotherset)
# you can use setup.difference(anotherset) to compare what setup has that anotherset doesn't, comparing 2 sets and vice versa
# you can also see what they have in common using the setup.intersection(another set) method

setup = {"controller", "monitor", "speaker"} # use curly braces to create a set

for item in setup:
    print(item)

