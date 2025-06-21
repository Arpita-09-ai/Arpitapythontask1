s=eval(input("enter list"))
l=[]
for i in range(len(s)):
    a=0
    if s[i]>1:
        for j in range(1,s[i]+1):
            if s[i]%j==0:
                a+=1
        if a==2:
            l.append(s[i])
print(l)
        
    
