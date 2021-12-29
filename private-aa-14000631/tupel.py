def add_item(my_tupel,item) :
    temp= list(my_tupel)
    temp.append(item)
    result= tuple(temp)
    return result

x= add_item((1,2,3),item=(6,8))
print(x)

def my_function(my_tuple, item):
    count = 0
    for i in my_tuple:
        if i == item:
            count += 1
    return count


# a = (5, 6, 7, 8, 7)
# b = 10
# print(my_function(a, b))

# -----------------------------
def remove_item(my_tuple, item):
#    a = []
#    for i in my_tuple:
#       if i != item:
#           a.append(i)
    a = [i for i in my_tuple if i != item]
    return tuple(a)


print(remove_item((1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 7), 4))
