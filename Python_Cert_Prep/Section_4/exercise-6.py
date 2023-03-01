# f

ans = 0

while ans != 1994:
    ans = int(input("When was Python 1.0 released? "))

    if ans > 1994:
        print('It was earlier than that!')
    elif ans < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
