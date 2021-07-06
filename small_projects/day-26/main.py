# with open("file1.txt") as file:
#     file1 = file.readlines()
# with open("file2.txt") as file2:
#     file2 = file2.readlines()
#
# result = [int(num) for num in file1 if num in file2]
#
# print(result)

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

# Write your code above 👆
print(result)

