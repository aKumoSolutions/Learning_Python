all = {'instructors': ['Ahmad', 'Abdul', 'Kris', 'Gulnaz', 'Esen'], 'members': ["Abdulhamid", "Ahmadyar", "Aiya", "Esenbek", "Gulnaz", "Kris", "Marlen", "Meerim", "Mohammad", "Salmon", "Simon"]}

both = [all['instructors'][person] for person in range(len(all['instructors'])) if all['instructors'][person] in all['members']]

# for person in range(len(all['instructors'])):
#     inst = all['instructors'][person]
#     if inst in all['members']:
#         both.append(inst)

# print(both)