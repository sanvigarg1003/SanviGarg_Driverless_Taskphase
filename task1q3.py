#formulatask1q3
class mylist:
    def selection_sort(self,string):
        for i in range(len(string)-1):
         min=i
         for j in range(i+1,len(string)):
           if string[j]<string[min]:
               min=j

        string[i],string[min]=string[min], string[i]
        return string

    
    def binary_search(self, arr, key):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==key:
                return mid
            elif arr[mid]<key:
                low=mid+1
            else :
                high=mid-1
        return -1
n=int(input("Enter number of strings"))
arr=[]
for i in range(n):
    arr.append(input("Enter string"))
arr.sort()
key=input("Enter string to search")
obj=mylist()
result=obj.binary_search(arr,key)
print("Sorted list",arr)
if result!=-1:
        print("String found at index", result)
else:
    print("String not found")
