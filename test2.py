list = ['one', 'two', 'three']


item = ",".join(str(element) for element in list)
print(type(item))


print(item.split(","))