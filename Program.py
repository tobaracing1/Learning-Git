#Program mengubah data list menjadi data unique

#Program untuk mengubah data
def set_change(uniq):
    him = set()
    for i in uniq:
        him.add(i)
    return him

#Contoh list yang akan diubah    
list1 = [1,2,3,3,3,3,4,5]

#Perintah Output ke layar User
print (list(set_change(list1)))