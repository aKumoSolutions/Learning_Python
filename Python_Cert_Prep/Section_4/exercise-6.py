# Ask the user to guess the year when Python 1.0 was released(the correct answer is 1994) with the following prompt:

# When was Python 1.0 released? << remember to add a space at the end of this prompt

# If the user answers 1994, show:

# Correct!

# and finish the program. If the user answers with a year later than 1994, show a hint and ask again for a new year on a new line:

# It was earlier than that!
# When was Python 1.0 released? << remember to add a space

# If the user answers with a year earlier than 1994, show a hint and ask again for a new year on a new line:

# It was later than that!
# When was Python 1.0 released? << remember to add a space


ans = 0

while ans != 1994:
    ans = int(input("When was Python 1.0 released? "))

    if ans > 1994:
        print('It was earlier than that!')
    elif ans < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
