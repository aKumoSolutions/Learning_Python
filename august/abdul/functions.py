data = []
def sum(y, x=5):
    r = x + y
    if r == 5:
        return "y is 0"
        
    data.append(r)
    return data


sum(y=1)
print(data)