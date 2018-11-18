#Printing of fibonaci sequence in a certain range
Last_number = int(input("Enter the last number : "))
num_of_fib = int(input("how many number should be generated between the range 1 and " + str(Last_number) + " : "))
Sum = [0, 1]
i = 1
a = 0
b = 1
c = 1
for i in range(1,num_of_fib):
                 if i < num_of_fib:
                     i = i+1
                     a = b
                     b = c
                     c = a + b    
                     if c < Last_number:
                         Sum.append(c)
                     else:
                         break
print("fibonaci sequence ")
print(Sum) 
