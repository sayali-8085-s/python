# read()


# f =open('n3.py')
# data = f.read()
# print(data)
# f.close()

# data = f.read(5)
# print(data)
# f.close()

# data = f.read(5000000)
# print(data)
# f.close()

# data = f.readlines()  # o/p data type list
# print(data)
# f.close()



# curssor current position - tell()
# print(f.tell())
# data = f.read(10)
# print(data)
# print(f.tell())
# f.close()



# check position of cursor for append
# f =open('n3.py','a')
# print(f.tell())

# # for write
# f =open('n3.py','w')
# print(f.tell())




# cursor movement - seek()
# f =open('n3.py')
# print(f.tell())

# data = f.read(10)
# print(data)
# f.seek(5)
# print(f.tell())
# data = f.read(10)
# print(data)

# f.close()
f =open('n3.py','rb')
print(f.tell())

data = f.read(5)
print(data)
f.seek(5,1)
print(f.tell())
data = f.read(10)
print(data)

f.close()
