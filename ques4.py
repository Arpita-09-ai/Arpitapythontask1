l=eval(input("enter list of tuples"))
s=eval(input("enter set"))
for i in l:
    if i[0] in s:
        print(i)
