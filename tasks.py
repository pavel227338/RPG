ababa = input("какая задача вас интересует?\n")
def math ():
    number = input("ведите число\n")
    number = int(number)
    number = number*2
    print(number)
fruits = ["ipple","pineapple","banana","avacado","youpple"]
def task_six(fruits,fruit):
    print(fruits)
    fruits.append("dragon fruit")
    print(fruits)
    del fruits[1]
    print(fruits)
spisok = [-7,5,6,-3,9,-4,7,2,-9,11]
def task_7(spisok):
    min = spisok[0]
    max = spisok[0]
    for element in spisok:
        if element < min:
            min = element
        if element > max:
            max = element
    return min,max
d = " "
a = "памагити"
b = "пажалуста"
def textmath (a,b,d):
    c = a + d + b
    return c
def task_9():
    for i in range(1,498):
        if i % 2 == 0:
            print (i)
quests = ["Паша","Артём","Олег","Юля","Костя","Кирилл"]
def task_13(quests):
    for i in range (1,6):
        print("привет ",quests[i])
a = input("")
a = int(a)
b = input("")
b = int(b)
def task_11(a,b):
    if a < b:
        for i in range (a,b+1,1):
            print (i)
    elif a > b:
        for i in range(a,b-1,-1):
            print (i)
    else:
        print(a)
if ababa == "1":
    math()
elif ababa == "2":
    task_six(fruits,"dragon fruit")
elif ababa == "3":
    min,max = task_7(spisok)
    print(min)
    print(max)
elif ababa == "4":
    c = textmath(a,b,d)
    print(c)
elif ababa == "5":
    task_9()
elif ababa == "6":
    task_13(quests)
elif ababa == "7":
    task_11(a,b)