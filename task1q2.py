#formulatask1q2
class mylist:
    def selection_sort(self,string):
        for i in range(len(string)-1):
         min=i
         for j in range(i+1,len(string)):
           if string[j]<string[min]:
               min=j

         string[i],string[min]=string[min], string[i]
        return string
    
n=int(input("Enter number of strings"))
string=[]
for i in range(n):
     string.append(input("Enter string"))
    
obj=mylist()
result=obj.selection_sort(string)
print(result)
    
