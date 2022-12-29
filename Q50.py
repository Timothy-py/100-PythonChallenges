# QUESTION 50
# Given array {2,4,6,10}
# target say (16)
# Find the number of possible subsets that will sum up to the target.
# Assumptions: i. all elements inside the array is non-negative.
# ii. You cannot repeat number.
# iii. if 0 is given as the target, the possible subset is 1 i.e {}.


def targeter(array=input("Enter array here: "), target=int(input("Enter target number here: "))):

    # clean the list/array supplied
    array_string = array.split(",")
    array_int = []
    for i in array_string:
        try:
            int(i)
        except ValueError as e:
            print(e, "\n" f"{i} is not an integer number")
        else:
            array_int.append(int(i))

    array_int = list(set(array_int))
    print(f"array_int = {array_int}")

    # FIRST ITERATION
    # iteratively generate and supply sub_array_int_list (as num_list) to sub_list_generator function
    # i.e in arr={a, b, c, d} it generates {a,b,c,d,}, {b,c,d}, {c,d}, {d}.
    generator = (array_int[i:] for i in range(len(array_int)))
    for i in range(len(array_int)):
        num_list = next(generator)

        # sub_list_generator_function
        # a generator to generate sub_list from num_list supplied from above
        # i.e num_list = {b,c,d}, sub_num_list = {b,c,d}, {c,d}, {d}
        gen = (num_list[_:] for _ in range(len(num_list)))

        # a variable to iteratively store num_list[0] from the for_loop below
        # and set it to empty again for the Second Iteration
        _head = []
        # print(_head)

        # SECOND ITERATION
        # perform the computations inside the for_loop for all the elm in num_list
        for _ in range(len(num_list)):

            # sub_list_generator
            # say sub_num_list = {b,c,d}
            sub_num_list = (next(gen, 0))

            # _head = [b,..]
            _head.append(sub_num_list[0])

            # sub_num_list becomes, {c,d}
            del(sub_num_list[0])

            # iteratively add the values in _head to sub_num_list and checks if it's equal to target
            for _ in sub_num_list:

                if sum(_head) + _ == target:
                    print(f"{_head} + {_} = {target}")


targeter()
