#my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#i = 0
#while True:
#    if my_list[i] == my_list[i + 1]:
#        del my_list[i]
#    elif (i + -1) == len(my_list):
#        break
#    i = i + 1


#print("The list with unique elements only:")
#print(my_list)

blocks = int(input("Number of Blocks: "))
i = 0
blocks_count = 0

while blocks_count < blocks:
    i = i + 1
    blocks_count = blocks_count + 1
    print(blocks_count)

if(blocks_count != blocks):
    i = i - 1
print("The height of the pyramid", i)

