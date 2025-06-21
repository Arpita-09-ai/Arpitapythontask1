l=[10,20,30,40,50]
if len(l)%2!=0:
    l.pop(int(len(l)/2))
else:
    l.pop(int(len(l)/2))
    l.pop(int(len(l)/2))
print(l)
