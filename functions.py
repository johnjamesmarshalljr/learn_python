def sayhi(name, age):
    # print(f"hey {name} you are {age} years old")
    print("hey %s you are %s years old" % (name, age))

# sayhi("jj", "34")


def cube(num):
    return num*num*num
    # return keyword breaks out of fn


result = cube(4)
print(result)
