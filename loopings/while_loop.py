"""
A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. 
The loop will continue to execute as long as the condition evaluates to True. 
Once the condition becomes False, the loop will stop executing.
"""

# Example of a while loop that counts from 1 to 5
# count = 1
# while count <= 5:
#     print('count')
#     count +=1
#     print('done')


# print 1 to 10 numbers

# i = 1
# while i <=10:
#     print(i)
#     i +=1

#  print 1 to 20 even numbers
# i = 1
# while i <= 20:
#     if i % 2 ==0:
#         print(i,end=" ")
#     i += 1


#  print 1 to 20 odd numbers
    
# i = int(input('enter number:'))

# while i <= 20:
#     if i % 2 != 0:
#         print(i,end=" ")
#     i += 1

"""
While problems
"""

# 1) 
# num = int(input("enter number:"))
# i = 1
# while i <= num:
#     print(i,end=" ")
#     i += 1
# print('Enter positive number')

# 2) print number from start to 1

# N = int(input('Enter number:'))
# i = N
# while N >= 1:
#     print(N,end=" ")
#     N -= 1


# 3) print number from start to end 
# start = int(input('enter start number:'))
# end = int(input('Enter end number:'))

# while start <= end:
#     print(start,end=" ")
#     start += 1
# print('\nDone')


# 4) sum of all number from 1 to 10
# num = int(input('Enter number:'))
# sum = 0
# while num <= 10:
#     sum += num
#     num += 1
# print(f'sum from 1 to 10: {sum}',end=" ")
   

# 5) product of all number from 1 to 10
# num = int(input('Enter number:'))
# product = 1
# while num <= 10:
#     product *= num
#     num += 1
# print(f'product from 1 to 10: {product}',end=" ")



# 6) number divisible by 7 from 1 to 100
# num = int(input('enter number:'))
# count = 0
# while num <= 100:
#     if num %7 == 0:
#         count += 1
#     num += 1
# print(f'Divisible by 7 : {count}')

# 6) same as 5 question but check divisible of 6 and 7 btw 1 to 200

# i = 1
# count = 0
# while i<=200:
#     if i%6==0 and i%7==0:
#         count +=1
#         print(i,end=" ")
#     i+=1
# print(f'\ncount of : {count}')


# 7) sum all number by 4 from 20 to 50

# i = 20 
# sum = 0

# while i <= 50:
#     if i%4==0:
#         sum += 1
#         print(i)
#     i+=1
# print(f'\nsum of number divisible by 4 from 20 to 50: {sum}')
 