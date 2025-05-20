# playing with loop
# have to calculate the height as per the no. of blocks, which keeps on increasing by one on each layer

block = int(input("No. of blocks: "))
height = 0
layer = 1

while block >= layer:
    print("*"*layer)
    block -= layer
    height += 1
    layer +=1

print("Final calculated height = ", height)
