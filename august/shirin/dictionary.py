
## key: value
## immutable: any data type

# student = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78
# }
# print(student)

abdul = {"name": "Abdul Sharif",
         "age": 24,
         "city": "Roselle",
         "engineer": True,
         "pets": [{
             "name": "tom cruize",
             "type": "rooster"},
            {
              "name"
         }]
         "hobbies": [
             "fishing",
             "ice skating",
             "snowboarding",
             "cooking"]
         }

# print(abdul['name'], abdul['age']) ## to access a key value pair, by providing a key name
# print(abdul.get('city'))

# if abdul.get('city'):
#     print("Abdul resides in", abdul['city'])
    
abdul['country'] = "United States"
# print(abdul)

# print(abdul.keys())
# print(abdul.values())

# for key in abdul.keys():
#     if abdul.get(key) == "Roselle":
#         print("key is:", key)
        
del(abdul['city'])
# print(abdul)
abdul.pop('engineer')
# print(abdul)

# print(abdul.items())

# for key, value in abdul.items():
#     print(key,":", value)

abdul['hobbies'].append('gardening')
print(abdul)
