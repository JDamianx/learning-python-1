numbers = [2, 5, 8, 9, 12, 15, 18, 21]
for i in range(len(numbers)):
    if i%2!=0:
        print(numbers[i])
    else:
        del numbers[i]