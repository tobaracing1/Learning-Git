#Program mengubah data list menjadi data unique
def set_change(uniq):
    him = set()
    for i in uniq:
        him.add(i)
    return him

list1 = [1,2,3,3,3,3,4,5]

print (set_change(list1))