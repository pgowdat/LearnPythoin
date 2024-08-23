# to make any changes in tuple , convert tuple into list and do changes 

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8) --> 3 in between index 4 and 8
#res = len(tuple1)
print('Count of 3 in tuple1 is:', res)