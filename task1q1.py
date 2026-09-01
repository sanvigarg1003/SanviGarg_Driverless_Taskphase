#formulatask1
n=int(input("Enter number of strings"))
strings=[]
for i in range(n):
       s=input("Enter string")
       strings.append(s)
count={}
for s in strings:
           for ch in s.lower():
               if ch in count:
                   count[ch]+=1
               else:
                       count[ch]=1
print(count)
