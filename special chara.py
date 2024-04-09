

str1=input("please enter your own string:")
i=0
vowl=''
for char in str1:
    if char in '[@_!#$%^&*()<>?/\|}{~:}]':
        vowl=vowl+char+','
        vowl=vowl[:-1]
        print("the special charecters are:",vowl)