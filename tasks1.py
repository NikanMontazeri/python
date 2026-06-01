
#task1
num = [10,20,30,40,50]
print(f"the list length is:{len(num)}")
print(f"the min is:{min(num)}")
print(f"the max is:{max(num)}")
#task2
print(30 in num)
#task3
x = [78,34,14,29,48,37,26,25,15,34,14,29,34]
x.sort()
print(x)
print(set(x))
print(sorted(set(x)))
#task4
print(num[1:4])
#task5
students = ["amir","ali","hosein","ehsan"]
for i in students:
    print("welcome to new university " + i)
#task6
for i in range(1,11,):
    print(i ** 3)
#task7
number = [2,5,7,34]
plus = 0
for i in number:
    plus += i  
    print(plus)
#task8
square = [o ** 2 for o in range(1,21)]
print(square)
#task9
#i dont know