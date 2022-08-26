# ascii ==> American Standard Coding Information and Interchange
# ascii values for lower case and upper case alphabets,and also for numbers
# a ---97             A ---65             0 ---48
# z ---122            Z ---90             9 ---57



# a=b"lokesh"
# print(a,type(a))
# print(list(a))  # here the bytes can give the ascii values of the string. (in a list form)
# print(tuple(a))   # here the bytes can give the ascii values of the string.(in a tuple form)
# print(set(a))   # here the bytes can give the ascii values of the string like ascending order .(in set form)

# c=b"lokesh"
# for a in c:
#     print(a)  # here the bytes wil give the ascii values in vertical order. 

# v=b"lokesh"
# print(type(v))
# v[0]=90   # TypeError: 'bytes' object does not support item assignment  {bcoz bytes are immutable sequnce(which modifications cannot be made or done.)}
# v[0]=65  # no modifications

# f=b'[1,2,4]'
# print(list(f))   # here string gives ascii values in list form. 

# print(ord('['))
# print(ord(']'))   # these are useful to know the ascii values symbols, numbers,alphabets
# print(chr(92))
# print(chr(44))