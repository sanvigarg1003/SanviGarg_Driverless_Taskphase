#formulatask1q6
size=int(input("Enter the size of hash table"))
hash_table=[[]for i in range(size)] 
n=int(input("Enter number of integers"))
for i in range(n):
     number=int(input("Enter the integers"))
     index=number%size
     bucket=hash_table[index]
     low=0
     high=len(bucket)
     while low<high:
      mid=(high+low)//2
      if number>bucket[mid]:
       low=mid+1
      else:
       high=mid
     bucket.insert(low, number)
print(hash_table)
