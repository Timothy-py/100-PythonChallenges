# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# This solution first initializes an empty list called triangle to store the rows of the triangle. It then iterates through the rows, starting from the first row, and generates each row based on the previous row. For the first two rows, it directly appends the row to the triangle list. For all other rows, it uses a loop to generate the row by adding the elements of the previous row and appending the result to the triangle list.

# For example, if numRows is 5, the function will generate the following triangle:

# [
#  [1],
# [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows):
    triangle = []

    for row in range(numRows):
        if row == 0:
            triangle.append([1])
        elif row == 1:
            triangle.append([1, 1])
        else:
            new_row = [1]
            prev_row = triangle[row-1]
            for i in range(len(prev_row)-1):
                new_row.append(prev_row[i] + prev_row[i+1])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
