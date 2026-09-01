#formulatask1q5
size=int(input("Enter the size of hash table"))
hash_table=[[]for i in range(size)] 
n=int(input("Enter number of integers"))
for i in range(n):
     number=int(input("Enter the integers"))
     index=number%size
     hash_table[index].append(number)
print(hash_table)
    
