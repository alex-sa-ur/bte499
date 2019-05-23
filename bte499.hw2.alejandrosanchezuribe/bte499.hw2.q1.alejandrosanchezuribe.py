# Author:       Alejandro Sanchez Uribe
# Date:         28 January 2019
# Class:        BTE 499
# Assignment:   Assignment 2 - Question 1

print('Assignment 2 - Question 1')

# a: g equals h squared
print('A.')
h = 8
g = h**2

print('\t{} is the square root of {}'
      .format(h, g))

# b: price conversion from cents (int) to dollars (float) and exam average
print('B.')
price = 4321

dollars = price // 100
cents = round(price - dollars * 100, 2)

print('\ti) {} dollars and {} cents'
      .format(dollars, cents))

exam1 = 80
exam2 = 100

average = round((exam1 + exam2) / 2, 2)

print('\tii) Exam average of scores {} and {}: {}'
      .format(exam1, exam2, average))

# c: second character of name
print('C.')
name = 'Alex'

secondChar = name[1]

print('\tThe second character of {} is {}'
      .format(name, secondChar))

# d: substring of s from indexes 0 to 8 (first 9 characters)
print('D.')
s = 'fromStartToNinthChar'

subS = s[:9]

print('\tThe substring \'{}\' from \'{}\' starts on the first character and ends in the 9th'
      .format(subS, s))

# e: first, middle, and last name initials
print('E.')
firstName = 'John'
middleName = 'Fitzgerald'
lastName = 'Kennedy'

initials = firstName[0] + middleName[0] + lastName[0]

print('\t{} {} {}\'s initials: {}'
      .format(firstName, middleName, lastName, initials))

# f: second word of a sentence
print('F.')
sentence = 'This is the value of a sentence.'

secondWord = sentence.split()[1]

print('\tThe second word of the sentence \'{}\' is \'{}\''
      .format(sentence, secondWord))

# g: initials with periods
print('G.')
given = 'John'
middle = 'Fitzgerald'
family = 'Kennedy'

initialsPeriod = '{}.{}.{}.'\
    .format(given[0], middle[0], family[0])

print('\t{} {} {}\'s initials: {}'
      .format(given, middle, family, initialsPeriod))

# h: phone number formatting
print('H.')
areaCode = 800
exchange = 555
lastFour = 1212

phoneNum = "-".join((str(areaCode), str(exchange), str(lastFour)))

print('\tThe formatted phone number is:', phoneNum)

# i: display inputted name and age
print('I.')
name = input('\tInput a name: ')
age = input('\tInput the age of {}: '.format(name.capitalize()))

nameAgeMessage = 'The age of {} is {}'.format(name.capitalize(), age)

print('\t ' + nameAgeMessage)

# j: greet inputted name
print('J.')
name = input('\tInput a name: ')

greeting = 'Greetings, {}!!!'.format(name.capitalize())

print('\t ' + greeting)

# k: siblings average age calculation
print('K.')
josh = eval(input('\tInput Josh\'s age: '))
cindy = eval(input('\tInput Cindy\'s age: '))
me = eval(input('\tInput your age: '))

average = (josh + cindy + me) / 3

print('\tAverage age: {0:.2f}'.format(average))

# l: replace plist index k with int value 15
print('L.')
plist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k = 3
print('\tk =', k)
print('\tOriginal plist:', plist)

plist[k] = 15

print('\tModified plist:', plist)


# m: associate first int element of play_list with twice the value of the last element
print('M.')
play_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\tOriginal play_list:', play_list)

play_list[0] = play_list[len(play_list) - 1] * 2

print('\tModified play_list:', play_list)

# n: add element to end of plist
print('N.')
plist = [1, 2, 3, 4]
print('\tOriginal plist:', plist)

plist.append(5)

print('\tModified plist:', plist)

# o: remove element at index k from alist
print('O.')
alist = [1, 2, 3, 4, 5, 6, 7, 8]
k = 6
print('\tk=', k)
print('\tOriginal alist:', alist)

del alist[k]

print('\tModified alist:', alist)

# p: remove first element from alist
print('P.')
alist = [1, 2]
print('\tOriginal alist:', alist)

del alist[0]

print('\tModified alist:', alist)

# q: remove 4th element from alist
print('Q.')
alist = [1, 2, 3, 4, 5]
print('\tOriginal alist:', alist)

del alist[3]

print('\tModified alist:', alist)

# r: concatenate plist1 and plist2 into plist3
print('R.')
plist1 = [1, 2, 3]
plist2 = [4, 5, 6]
print('\tplist1:', plist1)
print('\tplist2:', plist2)

plist3 = plist1 + plist2

print('\tplist3:', plist3)

# s: remove last element from alist
print('S.')
alist = [1, 2, 3, 4, 5, 6]
print('\tOriginal alist:', alist)

del alist[len(alist) - 1]

print('\tModified alist:', alist)

# t: remove last element from alist and associate that value to k
print('T.')
alist = [1, 2, 3]
print('\tOriginal alist:', alist)

k = alist.pop(len(alist) - 1)

print('\tModified alist:', alist)
print('\tk =', k)

# u & v: sort play_list
print('U. & V.')
play_list = [1, 4, 6, 2, 5, 3, 8, 7]
print('\tOriginal play_list:', play_list)

for i in range(len(play_list)):
    for j in range(i, len(play_list)):
        if play_list[i] > play_list[j]:
            play_list[i], play_list[j] = play_list[j], play_list[i]

print('\tModified play_list:', play_list)

# w: Replace elements in play_list (1-3)
print('W.')
play_list = ['bun', 'patty', 'lettuce', 'cheese', 'onions',
             'tomato', 'ketchup', 'mustard', 'pickles', 'top bun']
print('\tOriginal play_list:', play_list)

play_list[0:2] = 'spam', 'eggs', 'vikings'

print('\tModified play_list:', play_list)

# x: replace contents of indexes 5-8 in L1 with L2
print('X.')
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = ['A', 'B', 'C', 'D']
print('\tOriginal L1:', L1)
print('\tL2:', L2)

L1[5:9] = L2[:]

print('\tModified L1:', L1)

# y: evaluate the kth element of tuple t
print('Y.')
k = 2
t = 1, 2, 3, 4, 5

print('\tElement #{} from the tuple {} is:'.format(k, t), t[k-1])

# z: associate play_list with a list containing all elements of tuple t
print('Z.')
play_list = ['A', '2', 'Z', 'b', 'G']
t = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print('\tOriginal play_list:', play_list)
print('\tt:', t)

play_list = list(t)

print('\tModified play_list:', play_list)
