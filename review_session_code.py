''' Numbers '''
#%% use Python for standard mathematical operations
print(2 + 3)
print(2 * 3)
print(2 ** 3)

#%% names are case-sensitive
price = 40
Price = 60
print(price)
print(Price)

#%% update variables
price + 10
print(price)

price = price + 10
print(price)

price += 10
print(price)

price *= 2
print(price)

price /= 2
print(price)

#%% round a number
print(round(1.23456, 2))

print(int(0.3))
print(int(1.001))

print(int(0.9))
print(round(0.9))

#%% need to know about a function
?round
#%% use the type() function to check the type of a number
print(type(5))
print(type(2.3))
print(type(price))
#%%
''' Boolean Variables '''
#%% check for inequality
x = 5 < 3
print(x)
print(type(x))
#%% = vs. ==
x = 5
x == 5
#%% combine multiple conditions
x = (1<2) & (1>0)
print(x)

x = (1 < 2) | (1 > 2)
print(x)

''' == != > < <= >= '''

#%% use booleans in mathematical operations
x = 2 > 1
y = 10 + x
print(y)

x = 2 < 1
y = 10 + int(x)
print(y)
#%%
''' Strings '''
#%% This is a string
firm = 'Microsoft'
print(firm)

firm = "Microsoft"
print(firm)

print(type(firm))

#%% combine ("concatenate") strings
x = 'abc'
y = 'def'
z = x + y
print(z)
#%% we cannot add an integer or float to a string
a = 'stock'
b = 1
c = a + b
#%%
c = a + str(b)
print(c)
#%%
''' Lists '''
#%% collect multiple data points in a list
prices = [100, 104, 99, 98, 102, 105, 110]
print(prices)

print(type(prices))
#%% combine ("concatenate") lists
new_prices = prices + [120,130]
print(new_prices)
#%% access elements of a list
'''
prices = [100, 104, 99, 98, 102, 105, 110]
index:    0    1    2   3   4    5    6
backward:-7   -6   -5  -4  -3   -2   -1
'''
print(prices[0])
print(prices[1])
print(prices[-1])
print(prices[1:4])
print(prices[:3])
print(prices[3:])
print(prices[-3:])
print(prices[0:6:2]) # selects every 2nd element
print(prices[0::2])
print(prices[::2])
print(prices[::-1]) # reverse list

#%% modify elements of the list
prices[0] = 101
print(prices)

prices[4:6] = [104,106]
print(prices)
#%% create a sequences
x = list(range(10))
print(x)

print(type(x))

x = list(range(2,6))
print(x)

x = list(range(20, 60, 5))
print(x)

#%% some functions for the lists
prices = [100, 104, 99, 98, 102, 105, 110]
prices.append(80)

prices.remove(104) # remove 1st occurence of "104"

prices.sort()

prices.reverse()

#%%
''' Tuples '''
#%%
# empty tuple
my_tuple = ()
print(my_tuple)

# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("Hello", [8, 4, 6], (1, 2, 3))
print(my_tuple)
#%% access elements of a tuple
print(my_tuple[0])
print(my_tuple[1])

#%% tuples are immutable
my_tuple = (1, 2, 3)
my_tuple[0] = 10

my_tuple.append(10)

#%%
''' If Statements '''
#%% if else
price = 60

if (price < 50):
    print('price is below 50!')
    print('buy!!')
else:                               # The else statement is optional
    print('price is above 50!')
    print('sell!!')

#%% multiple tests
price = 60

if (price < 60): 
    print('buy!') # if price >= 60 go to next line
elif (price < 70): 
    print('hold') # if price >= 70 go to next line (elif is short for "else if")
else: 
    print('sell!')
