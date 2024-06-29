num = [1, 2, 4, 6, 9, 8, 10, 3]
## sorts the original (num) list
# num.sort()

## saves a sorted version of the (num) list
copied = sorted(num)
copied.append(5)
copied.sort(reverse=True)
print(copied)
