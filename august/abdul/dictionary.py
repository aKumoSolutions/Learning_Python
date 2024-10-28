student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

##   key: value
##  immutable : any data type
abdul = {
    "name": "Abdul Sharif", 
    "age": 24, 
    "city": "Roselle",
    "engineer": True,
    "pets": [
        {
            'name': 'tom cruize', 
            'type': 'rooster'
        }, 
        {
            'name': 'john wick',
            'type': 'chicken'
        }],
    "hobbies": [
        "fishing", 
        "ice skating", 
        "snowboarding", 
        "cooking"
        ]
    }

abdul['hobbies'].append("gardening")
abdul['pets'].append({'name': 'cookie', 'type': 'cat'})
# abdul['pets'][2]['color'] = "black"
# print(abdul['pets'][2])
for pet in abdul['pets']:
    if pet['type'] == 'cat' and pet['name'] == 'cookie':
        pet['color'] = 'black'

    print(pet)
    



# if abdul.get('city'):
#     print("Abdul resides in", abdul['city'])

# abdul['city'] = "Des Plaines"

# for key in abdul.keys():
#     if abdul.get(key) == 'Des Plaines':
#         print("key is:", key)

del(abdul['city'])
abdul.pop('engineer')
# print(abdul)

# for key, value in abdul.items():
#     print(key, value)