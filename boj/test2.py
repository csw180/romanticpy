import collections

RowType = collections.namedtuple("Row", ["a", "b", "c"])  
print(type(RowType))
print(RowType)
row = RowType(a=1,b=2,c=3)
print(type(row))
print(row)