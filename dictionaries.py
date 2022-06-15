phonebook = {}

phonebook["ganesh"] = 7075170297
phonebook["neha"] = 9491036331
phonebook["nirmala"] = 7731834366
print(phonebook)

phonebook = {
             "ganesh":7075170297,
             "neha":9491036331,
             "nirmala":7731834366
             }
print(phonebook)

for names, numbers in phonebook.items():
    print("phonebook have name %s and number %d"%(names,numbers))

del phonebook["nirmala"]
print(phonebook)

phonebook.pop("ganesh")
print(phonebook)
