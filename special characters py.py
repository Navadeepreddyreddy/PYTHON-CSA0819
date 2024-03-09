def n(statement):
    special_charaters = "!@#$%^&*()_-+=[]{}|;:,.<>/'\"\\"
    count=0
    for char in statement:
        if char in special_charaters:
            count+=1
    return count
statement = input("enter a statement:")
special_count = n(statement)
print("no.of special charaters:",special_count)
