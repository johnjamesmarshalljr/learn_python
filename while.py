# i = -1
# while i <= 10:
#     print(i)
#     i += 1


str = "string"


def py_break(word):
    for val in word:
        if val == "i":
            break
        print(val)
    print("the end")


py_break(str)
