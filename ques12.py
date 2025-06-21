a=input('enter string')
s=''
i=0
while i<len(a):
    s+=a[len(a)-1-i]
    i+=1
if(s==a):
    print('pallindrome')
else:
    print('not pallindrome')
    
