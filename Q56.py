# QUESTION 56
# Please write a binary search function which searches an item in a sorted list. The function should return
# the index of element to be searched in the list.

list_input = sorted(input("Enter list item here : ").split(','))
target = input("Enter the target element to find here : ")

print(list_input)


def bin_search(first_elm=0, last_elm=len(list_input) - 1, list_input=list_input, target=target):

    if first_elm > last_elm:
        print('Empty list bro!')
        return False

    else:
        mid_elm = (first_elm + last_elm) // 2

        if target == list_input[mid_elm]:
            print(f"Searching...")
            print(f"Element found in index {mid_elm}")
            return True
        elif target < list_input[mid_elm]:
            print(f"Searching...")
            return bin_search(first_elm=first_elm, last_elm=mid_elm - 1)

        elif target > list_input[mid_elm]:
            print(f"Searching...")
            return bin_search(first_elm=mid_elm + 1, last_elm=last_elm)


bin_search()
