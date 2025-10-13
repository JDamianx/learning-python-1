# 1 zadanie
# numbers = [3, 6, 7, 8, 11, 12, 13, 14]
# # [3, 0, 7, 0, 11, 0, 13, 0]
# for i in range(len(numbers)-1,-1,-1):
#     if numbers[i]%2==0:
#         numbers[i]=0
# print(numbers)

# 2zadanie
data = ["a", "b", "c", "d", "e", "f", "g"]

for i in range(len(data)-1, 0, -2):  # od końca, aż do indeksu 1
    del data[i]
    print(data)6
print(data)
