import math
# QUESTION 46
# Listen to this story, a boy and his father, a programmer are playing with wooden blocks.
# They a're building a pyramid, their pyramid is a bit weird, as it's actually a pyramid-shaped
# wall -  it's flat. The pyramid is stacked according to one simple principle, each lower layer
# contains one block more than the layer above.
# Your task is to write a program which reads the number of blocks the builders have, and outputs
# the  height of the pyramid that can be built using these blocks.
# NOTE: The height is measured by the number of fully completed layers - if the builders doesn't
# have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.


# SOLUTION 1
def pyrabuilder(blocks=int(input("Enter the number of blocks you have : "))):

    init_pyramid = []
    final_pyramid = []

    mid_num = math.ceil(blocks/2)
    list_mid_num = [i for i in range(1, mid_num+1)]

    for num in list_mid_num:
        init_pyramid.append(num)
        if sum(init_pyramid) == blocks:
            break
        elif sum(init_pyramid) > blocks:
            break
        else:
            continue

    size = len(init_pyramid)+1
    for i in range(1, size):
        final_pyramid.append(init_pyramid.pop())

        if sum(final_pyramid) == blocks:
            print(f"Pyramid = {final_pyramid} \nHeight = {len(final_pyramid)}")
            for i in final_pyramid:
                print("*" * i)
            break
        elif sum(final_pyramid) > blocks:
            print(
                f"Pyramid = {final_pyramid[:-1]} \nHeight = {len(final_pyramid)-1}")
            for i in final_pyramid[:-1]:
                print("*" * i)
            break
        else:
            continue


pyrabuilder()


# SOLUTION 2
def pyramid_height(num_blocks):
    height = 0
    blocks_needed = 0
    while num_blocks >= blocks_needed:
        height += 1
        blocks_needed += height
    return height - 1


print(pyramid_height(4))  # Outputs: 2
print(pyramid_height(10))  # Outputs: 4
print(pyramid_height(20))  # Outputs: 7
