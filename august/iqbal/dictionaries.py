# # # # student_grades = {
# # # #     'Alice': 85,
# # # #     'Bob': 92,
# # # #     'Charlie': 78
# # # # }




# # iqbal = {
# #     'name': 'mohammad iqbal',
# #     'age': 34,
# #     'occupation': 'engineer',
# #     'city': 'New York',
# #     'engineer': True,
# #     'hobbies': [
# #         'fishing',
# #         'ice skating',
# #         'snowboarding',
# #         'cooking'
# #     ]
# # }

# # iqbal['hobbies'].append('gardening')
# # print(type(iqbal))
# # if iqbal.get('city'):
# #     print('iqbal resides in', iqbal['city'])
# # iqbal['city'] = 'new york'
# # for keys in iqbal.valuable():
# #     if value == 'new york':
# #         print('key is:', key)
# # del(iqbal['city'])
# # print(iqbal.pop('engineer'))
# # print(iqbal)


# iqbal = {
#     'name': 'mohammad iqbal',
#     'age': 34,
#     'occupation': 'engineer',
#     'city': 'New York',
#     'engineer': True,
#     'hobbies': [
#         'fishing',
#         'ice skating',
#         'snowboarding',
#         'cooking'
#     ]
# }

# iqbal['hobbies'].append('gardening')
# print(type(iqbal))

# if iqbal.get('city'):
#     print('iqbal resides in', iqbal['city'])

# iqbal['city'] = 'new york'

# for value in iqbal.values():
#     if value == 'new york':
#         print('key is:', key)

# del(iqbal['city'])
# print(iqbal.pop('engineer'))
# print(iqbal)


iqbal = {
    'name': 'mohammad iqbal',
    'age': 34,
    'occupation': 'engineer',
    'city': 'New York',
    'engineer': True,
    'hobbies': [
        'fishing',
        'ice skating',
        'snowboarding',
        'cooking'
    ]
}

iqbal['hobbies'].append('gardening')
print(type(iqbal))

if iqbal.get('city'):
    print('iqbal resides in', iqbal['city'])

iqbal['city'] = 'new york'

# Iterate over keys and values together
for key, value in iqbal.items():
    if value == 'new york':
        print('key is:', key)

del(iqbal['city'])
print(iqbal.pop('engineer'))
print(iqbal)
