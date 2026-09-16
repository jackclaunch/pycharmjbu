myDictionary = {"name1": "Justus",
                "name2": "Jim",
                "name3": "Joe"
                }
print(myDictionary)

myDictionary.update({"name4": "Jemi",
                     "name5": "Jack"})

del myDictionary["name2"]
del myDictionary["name3"]

myDictionary.update({"name4": "Jim",})
#OR
myDictionary["name4"] = "Melba"
print(myDictionary)