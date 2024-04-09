string_1 = input("Please Enter Your first String : ")
string_2 = input("Please Enter Your second String : ")

for i in range(len(string_2)):
    if string_1[i] == string_2[i]:
        print(f'the string matched at index - {i} : {string_1[i]}')