'''Exercise 01
Let us say your expense for every month are listed below,
    i. January - 2200
    ii. February - 2350
    iii. March - 2600
    iv. April - 2130
    v. May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this '''


#1. 
expense = [2200,2350,2600, 2130, 2190]

extra_feb = expense[1] - expense[0]

print(f"The extra amount spent in February compare to January is {extra_feb}")

#2.
total_expense = expense[0] + expense[1] + expense[2]

print(f"The total expense in first quarter of the year is {total_expense}") 

#3.
for i in range(len(expense)):
    if (i == 2000):
        print(f"Exact 2000 is {i}")
    else:
        print("No spent 2000 in the year exact")


#4.
expense.insert(5,1980)
print(f"After June Month {expense}")

#5.
expense[3] = expense[3] -200

print(f"After get refund on month April: {expense}")


'''Exercise 02
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange 
   (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order 
(Hint. Use dir() functions to list down all functions available in list)'''


heros=['spider man','thor','hulk','iron man','captain america']

#1.
print(f'Length of the list of heroes {len(heros)}')

#2.
heros.insert(5,'black panther')
print(f"After adding in the last index {heros}")

#3.
heros.remove('black panther')
heros.insert(3,'black panther')

print(f"first remove then insert and final heros {heros}")

#4.
heros[1:3]=['doctor strange']
print(heros)

#5.
heros.sort()
print(f"After soprting {heros}")


'''Exercise 3
Create a list of all odd numbers between 1 and a max number.
    Max number is something you need to take from a user using input() function'''



max_num = int(input('Max Number: '))

odd_list = [i for i in range(1,max_num+1) if i%2!=0]

print(f"Odd List: {odd_list}")
        


