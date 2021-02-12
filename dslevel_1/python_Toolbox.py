  #--  --  --  -- Python Data Science Toolbox (Part 1)
# Used for Data Scientist Training Path 
#FYI it's a compilation of how to work
#with different commands.

### Writing your own functions
### --------------------------------------------------------
### ---> Strings in python
# Execute the following code in the shell:
# object1 = "data" + "analysis" + "visualization"
# object2 = 1 * 3
# object3 = "1" * 3
# What are the values in object1, object2, and object3, respectively?
# R/ object1 contains "dataanalysisvisualization", object2 contains 3, object3 contains "111"


### --------------------------------------------------------
###---> Recapping built-in functions
# Assign str(x) to a variable y1: y1 = str(x)
# Assign print(x) to a variable y2: y2 = print(x)
# Check the types of the variables x, y1, and y2.
# What are the types of x, y1, and y2?
## R/ # x is a float, y1 is a str, and y2 is a NoneType.


### --------------------------------------------------------
### ---> Write a simple function
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'
    # Print shout_word
    print(shout_word)
# Call shout
shout()


### --------------------------------------------------------
### ----> Single-parameter functions
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Print shout_word
    print(shout_word)
# Call shout with the string 'congratulations'
shout('congratulations')


### --------------------------------------------------------
###-----> Functions that return single values
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Replace print with return
    return shout_word
# Pass 'congratulations' to shout: yell
yell = shout('congratulations')
# Print yell
print(yell)


### --------------------------------------------------------
#### ----> Functions with multiple parameters
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'  
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!' 
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2
    # Return new_shout
    return new_shout
# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')
# Print yell
print(yell)


### --------------------------------------------------------
####-----> A brief introduction to tuples
nums = (3, 4, 6)
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums
# Construct even_nums
even_nums = (2, num2, num3)
## printing
print(even_nums)


### --------------------------------------------------------
#### -----> Functions that return multiple values
def shout_all(word1, word2):   
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'  
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)
    # Return shout_words
    return shout_words
# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')
# Print yell1 and yell2
print(yell1)
print(yell2)


### --------------------------------------------------------
#### -----> Bringing it all together --- ex#0
# Import pandas
import pandas as pd
# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')
# Initialize an empty dictionary: langs_count
langs_count = {}
# Extract column from DataFrame: col
col = df['lang']
# Iterate over lang column in DataFrame
for entry in col:
    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
# Print the populated dictionary
print(langs_count)


### --------------------------------------------------------
#### -----> Bringing it all together --- ex#1
# Import pandas
import pandas as pd
# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    # Initialize an empty dictionary: langs_count
    langs_count = {} 
    # Extract column from DataFrame: col
    col = df[col_name]
    # Iterate over lang column in DataFrame
    for entry in col:
        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1
    # Return the langs_count dictionary
    return langs_count
# Call count_entries(): result
result = count_entries(tweets_df, 'lang')
# Print the result
print(result)


### --------------------------------------------------------
### ----> Pop quiz on understanding scope
# The variable num has been predefined as 5, alongside the following function definitions:
# def func1():
#     num = 3
#     print(num)
# def func2():
#     global num
#     double_num = num * 2
#     num = 6
#     print(double_num)
# Try calling func1() and func2() in the shell, then answer the following questions:
# What are the values printed out when you call func1() and func2()?
# What is the value of num in the global scope after calling func1() and func2()?
## R/ func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 6.


### --------------------------------------------------------
### ----> The keyword global
# Create a string: team
team = "teen titans"
# Define change_team()
def change_team():
    """Change the value of the global variable team."""
    # Use team in global scope
    global team
    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)
# Call change_team()
change_team()
# Print team
print(team)

### --------------------------------------------------------
### ----> Python's built-in scope
# Here you're going to check out Python's built-in scope, 
# which is really just a built-in module called builtins. 
# However, to query builtins, you'll need to import builtins 
# 'because the name builtins is not itself built in…No, 
# I’m serious!' (Learning Python, 5th edition, Mark Lutz).
# After executing import builtins in the IPython Shell, 
# execute dir(builtins) to print a list of all the names in 
# the module builtins. Have a look and you'll see a bunch of
# names that you'll recognize! Which of the following names
# is NOT in the module builtins?
### R/ ----> 'array'


### --------------------------------------------------------
###----> Nested Functions I
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    # Return a tuple of strings
    return (inner(word1), inner(word2) ,inner(word3))
# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


### --------------------------------------------------------
### ----> Nested Functions II
# Define echo
def echo(n):
    """Return the inner_echo function."""
    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word
    # Return inner_echo
    return inner_echo
# Call echo: twice
twice = echo(2)
# Call echo: thrice
thrice = echo(3)
# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))


### --------------------------------------------------------
### ---> The keyword nonlocal and nested functions
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""  
    # Concatenate word with itself: echo_word
    echo_word = word * 2 
    #Print echo_word
    print(echo_word)
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        #Use echo_word in nonlocal scope
        nonlocal echo_word     
        #Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'  
    # Call function shout()
    shout()  
    #Print echo_word
    print(echo_word)
#Call function echo_shout() with argument 'hello'    
echo_shout('hello')


### --------------------------------------------------------
####-----> Functions with one default argument
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')
# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo('Hey', 5)
# Print no_echo and with_echo
print(no_echo)
print(with_echo)


### --------------------------------------------------------
####----> Functions with multiple default arguments
# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    # Return echo_word_new
    return echo_word_new
# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', 5, True)
# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey', intense=True)
# Print values
print(with_big_echo)
print(big_no_echo)


### --------------------------------------------------------
### -----> Functions with variable-length arguments (*args)
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge
    hodgepodge = ""
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge
    return hodgepodge
# Call gibberish() with one string: one_word
one_word = gibberish('luke')
# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")
# Print one_word and many_words
print(one_word)
print(many_words)


### --------------------------------------------------------
###-----> Functions with variable-length keyword arguments (**kwargs)
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)
    print("\nEND REPORT")
# First call to report_status()
report_status(name='luke', affiliation='jedi', status='missing')
# Second call to report_status()
report_status(name='anakin', affiliation='sith lord', status='deceased')



### --------------------------------------------------------
###->>> Bringing it all together - ex#0
# Import pandas
import pandas as pd
# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}   
    # Extract column from DataFrame: col
    col = df[col_name]
    # Iterate over the column in DataFrame
    for entry in col:
        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
    # Return the cols_count dictionary
    return cols_count
# Call count_entries(): result1
result1 = count_entries(tweets_df, col_name='lang')
# Call count_entries(): result2
result2 = count_entries(tweets_df, col_name='source')
# Print result1 and result2
print(result1)
print(result2)


### --------------------------------------------------------
###->>> Bringing it all together - ex#1
# Import pandas
import pandas as pd
# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')
# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""  
    #Initialize an empty dictionary: cols_count
    cols_count = {}   
    # Iterate over column names in args
    for col_name in args:
        # Extract column from DataFrame: col
        col = df[col_name] 
        # Iterate over the column in DataFrame
        for entry in col:
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    # Return the cols_count dictionary
    return cols_count
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')
# Print result1 and result2
print(result1)
print(result2)


### --------------------------------------------------------
##---->>> Pop quiz on lambda functions
#  Recall what you know about lambda functions and answer 
# the following questions:
# How would you write a lambda function add_bangs that 
# adds three exclamation points '!!!' to the end of a string a?
# How would you call add_bangs with the argument 'hello'?
# You may use the IPython shell to test your code.
### R/ The lambda function definition is: add_bangs = 
# (lambda a: a + '!!!'), and the function call is: add_bangs('hello').


### --------------------------------------------------------
# ------>>>>   Writing a lambda function you already know
# Define echo_word as a lambda function: echo_word
echo_word = lambda word1, echo: word1 * echo
# Call echo_word: result
result = echo_word('hey', 5)
# Print result
print(result)


### --------------------------------------------------------
###---> Map() and lambda functions
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]
# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda a: a +'!!!', spells)
# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)
# Convert shout_spells into a list and print it
print(shout_spells_list)


### --------------------------------------------------------
###----->>>> Filter() and lambda functions
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6 , fellowship)
# Convert result to a list: result_list
result_list = list(result)
# Convert result into a list and print it
print(result_list)


### --------------------------------------------------------
####------>>>> Reduce() and lambda functions
# Import reduce from functools
from functools import reduce
# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)
# Print the result
print(result)


### --------------------------------------------------------
####------> Pop quiz about errors
# Take a look at the following function calls to len():
# len('There is a beast in every man and it stirs when you put a sword in his hand.')
# len(['robb', 'sansa', 'arya', 'eddard', 'jon'])
# len(525600)
# len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))
# Which of the function calls raises an error and what type of error is raised?
### R/ The call len(525600) raises a TypeError.


### --------------------------------------------------------
###--------->>>> Error handling with try-except
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words = ""
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    # Return shout_words
    return shout_words
# Call shout_echo
shout_echo("particle", echo="accelerator")


### --------------------------------------------------------
####-------->>>>> Error handling by raising an error
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
# Call shout_echo
shout_echo("particle", echo=5)


### --------------------------------------------------------
####-------->>>>> Bringing it all together - ex#0
# Import pandas
import pandas as pd
# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])
# Create list from filter object result: res_list
res_list = list(result)
# Print all retweets in res_list
for tweet in res_list:
    print(tweet)


### --------------------------------------------------------
####-------->>>>> Bringing it all together - ex#1
# Import pandas
import pandas as pd
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name] 
        # Iterate over the column in dataframe
        for entry in col:
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
        # Return the cols_count dictionary
        return cols_count
    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# Print result1
print(result1)
# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang1')

### --------------------------------------------------------
####-------->>>>> Bringing it all together - ex#2
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""  
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')
    # Initialize an empty dictionary: cols_count
    cols_count = {}   
    # Extract column from DataFrame: col
    col = df[col_name]    
    # Iterate over the column in DataFrame
    for entry in col:
        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1      
        # Return the cols_count dictionary
    return cols_count
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# Print result1
print(result1)


### --------------------------------------------------------
##### -----> Bringing it all together: testing your error handling skills
# You have just written error handling into your count_entries() function so that,
# when the user passes the function a column (as 2nd argument) NOT contained
# in the DataFrame (1st argument), a ValueError is thrown. You're now going 
# to play with this function: it is loaded into pre-exercise code, as is the 
# DataFrame tweets_df. Try calling count_entries(tweets_df, 'lang') to confirm
# that the function behaves as it should. Then call count_entries(tweets_df, 
# 'lang1'): what is the last line of the output?
# R/ 'ValueError: The DataFrame does not have a lang1 column.'