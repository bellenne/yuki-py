def task1_1():
    string = ""
    for i in range(1, 22):
        if i % 2 != 0:
            string += f"{i}, "
    print(string)

def task1_2():
    string = ""
    i = 1
    while i <=21:
        string += f"{i}, "
        i+=2
    print(string)

print("Availabled task number: 1_1,1_2")
functions = {"1_1": task1_1, "1_2":task1_2,}
functions[ input("Input task number for result output:")]()