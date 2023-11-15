clear
 #variables
#example1:variables are containers to store the data values python has no command for declaring the variable.a variable can create the moment you first assign the value
'''
x=2      #x is int
y="Sri"  #y is str
print(x)
print(y)     '''

#example2 Variables do not need to be declared with any particular type, and can even change type after they have been set.
'''
x=2
x="sally"
print(x)
          '''  


 #casting :to specify a data variable
'''
x=int(1)
y=str(2)
z=float(1)
print(x,y,z)   

output:1 2 1.0
            '''

#GET THE TYPE:can get the data type of a variable the type() function

'''x=2
y=2.0
z="sri"
a=""
print(type(x))
print(type(y))
print(type(z))
print(type(a))

output:
<class 'int'>
<class 'float'>
<class 'str'>
<class 'str'>  '''
  
#Variable names are case sensitive strings
'''
a=4
A="sri" 
print(a,A)
here a will not over write A  '''


#variable names
#1)must start with letter(a-z) or underscope(_),alpha numeric (0-9)
#2)cant start with number 
#case  sensitive(SRI,sri,Sri) are threee diff variables
#variable cant be a keyword 
'''
myvar="sri"
MY_var="sri"
Myvar="sri"
mYvar="sri"
_mYVar="sri"
_my_var="sri"
print(myvar)
print(MY_var)
print(MY_var)
print(MY_var)
print(_mYVar)   '''

#Illegal variable names:
'''
2myvar = "sri"
my-var = "sri"
my var = "sri"       '''


#camel case -> Each word, except the first, starts with a capital letter:
'''myVariableName="sri"

#pascal case->Each word starts with a capital letter:
MyVariableName = "Sri"

#snake case->Each word is separated by an underscore character:
my_variable_name="sri"
                            '''

#Global variables
'''
create a variable outside of a func & use it inside the func.

x="Ganesha"
def myfunc():
    print("sri"+x)
myfunc()
                            '''


