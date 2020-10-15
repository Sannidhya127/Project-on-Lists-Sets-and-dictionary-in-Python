
a = int(input("Enter the number of items you want\n"))
b = int(input("Enter 1 for list, 2 for dict, 3 for set\n"))
list1 = [i for i in range(a) if b == 1]
if b == 1:
    print(list1)

dict1 = {i: f"item {i}" for i in range(a) if b == 2}
if b == 2:
    print(dict1)

set1 = {i for i in range(a) if b == 3}
if b == 3:
    print(set1)
# Branch access
