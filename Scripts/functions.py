actors = [
  {
    "name": "Catherine Missal",
    "rating": 4875,
    "image_path": "/g3fsRgEoMxaqPayIMtGDWERqJ6A.jpg",
    "alternative_name": "null",
    "objectID": "551486300"
  },
  {
    "name": "Monica Bellucci",
    "rating": 3956,
    "image_path": "/z3sLuRKP7hQVrvSTsqdLjGSldwG.jpg",
    "alternative_name": "Monica Anna Maria Bellucci",
    "objectID": "551486310"
  },
  {
    "name": "Michael Doven",
    "rating": 2647,
    "image_path": "/fkHxoBAvAkqHxzoP1ukcbPnaaUi.jpg",
    "alternative_name": "null",
    "objectID": "551486320"
  },
  {
    "name": "Jasmine Reate",
    "rating": 2378,
    "image_path": "/qgI4agu15xBlnWkZEVpZhGFsV4Y.jpg",
    "alternative_name": "J.L. Reate",
    "objectID": "551486330"
  },
  {
    "name": "Tom Cruise",
    "rating": 2237,
    "image_path": "/3oWEuo0e8Nx8JvkqYCDec2iMY6K.jpg",
    "alternative_name": "null",
    "objectID": "551486340"
  },
  {
    "name": "Scarlett Johansson",
    "rating": 2128,
    "image_path": "/f3c1rwcOoeU0v6Ak5loUvMyifR0.jpg",
    "alternative_name": "Scarlett Johanssen",
    "objectID": "551486350"
  },
  {
    "name": "Anna Raadsveld",
    "rating": 1972,
    "image_path": "/hNeOrwFVEfjUgRsjSUNU6t1gt2N.jpg",
    "alternative_name": "null",
    "objectID": "551486360"
  },
  {
    "name": "Jason Statham",
    "rating": 1719,
    "image_path": "/PhWiWgasncGWD9LdbsGcmxkV4r.jpg",
    "alternative_name": "null",
    "objectID": "551486370"
  },
  {
    "name": "Emilia Clarke",
    "rating": 1585,
    "image_path": "/xMIjXRUkxpQs2o5VI3Om3yn6hNV.jpg",
    "alternative_name": "null",
    "objectID": "551486380"
  },
  {
    "name": "Wentworth Miller",
    "rating": 1579,
    "image_path": "/z5qjqYgWfZsBrLWWm9jMRSJOtQ2.jpg",
    "alternative_name": "null",
    "objectID": "551486390"
  },
  {
    "name": "Dwayne Johnson",
    "rating": 1568,
    "image_path": "/akweMz59qsSoPUJYe7QpjAc2rQp.jpg",
    "alternative_name": "The Rock",
    "objectID": "551486400"
  },
  {
    "name": "Rose Byrne",
    "rating": 1526,
    "image_path": "/fOQLAPDvqSDq4ktR7Xk8DIpzGdY.jpg",
    "alternative_name": "Mary Rose Byrne",
    "objectID": "551486410"
  },
  {
    "name": "Rachel McAdams",
    "rating": 1519,
    "image_path": "/wqSznVIPp0YDFCuZ9jjbrzDyJhV.jpg",
    "alternative_name": "Rachel Anne McAdams",
    "objectID": "551486420"
  },
  {
    "name": "Michelle Rodriguez",
    "rating": 1439,
    "image_path": "/v37VK0MNuRuJOCKPKJcZAJXRA5r.jpg",
    "alternative_name": "Michelle Rodríguez",
    "objectID": "551486430"
  },
  {
    "name": "Tom Hanks",
    "rating": 1392,
    "image_path": "/a14CNByTYALAPSGlwlmfHILpEIW.jpg",
    "alternative_name": "null",
    "objectID": "551486440"
  },
  {
    "name": "Jake Gyllenhaal",
    "rating": 1312,
    "image_path": "/wRgIPBzVzIIhWcdJAduPOKJJHsL.jpg",
    "alternative_name": "null",
    "objectID": "551486450"
  },
  {
    "name": "Tom Hardy",
    "rating": 1279,
    "image_path": "/5KwHVwrr982YSsCf4HaSFMLrsYf.jpg",
    "alternative_name": "null",
    "objectID": "551486460"
  },
  {
    "name": "Chloë Grace Moretz",
    "rating": 1266,
    "image_path": "/wYaBEV3SOYaJbo6FDKpQW9hlMWt.jpg",
    "alternative_name": "null",
    "objectID": "551486470"
  },
  {
    "name": "Johnny Depp",
    "rating": 1250,
    "image_path": "/ctaca3ALycPP0vPhRSYK5DTBEPF.jpg",
    "alternative_name": "John Christopher Depp II",
    "objectID": "551486490"
  },
  {
    "name": "Arnold Schwarzenegger",
    "rating": 1250,
    "image_path": "/3cWGPgdJn1s4O2Rvo6zN7yHkzOe.jpg",
    "alternative_name": "null",
    "objectID": "551486480"
  },
  {
    "name": "Sarah Wayne Callies",
    "rating": 1223,
    "image_path": "/1WTsRFbvxU9lOWonAigOO9UCxmY.jpg",
    "alternative_name": "null",
    "objectID": "551486500"
  },
  {
    "name": "Vincent Cassel",
    "rating": 1190,
    "image_path": "/yTTyX7xziiMibm0nzcH5z6xxLLv.jpg",
    "alternative_name": "null",
    "objectID": "551486510"
  }
]


def find_actor(actors: list, name: str):
    x = 0
    for actor in actors:
        if name in actor['name']:
            x = x + 1
            print(actor['name'])
    return f"We found {x} number of {name}"

# find_actor(actors=actors, name="Tom")


def function_1(name, age, pet):
    print(name, age, pet)

# function_1(name="abdul", age=22, pet="cookie")
    

def function_2(name: str, age: int, pet: str):
    print(name, age, pet)
    
def function_3(*args):
    for i in args:
        print(i)

# function_3("abdul", 22, "cookie")

def function_4(**kwargs):
    if 'name' in kwargs:
        print("name exists")

    print(kwargs['name'])
    print(kwargs['age'])
    
# function_4(name="Abdul", age=22)