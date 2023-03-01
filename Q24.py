# Write a valid HTML + Python Page that will count numbers from 1 to 1,000,000?
# i.    Display every 10th number in the series in Bold
# ii.   Display every 3rd number in the series in Italics.
# iii.  Bonus: Underline every Prime Number in this series.

# < !DOCTYPE
# html >
# < html >
# < head >
# < title > Intenship < / title >
# < / head >
#
# < body >
#
# < b > tenth_num = [num for num in range(1, 10000001) if str(num).endswith('0')] < / b >
#
# < i > third_num = [num for num in range(1, 10000001) if num % 3 == 0] < i / >
#
# remainder_list = []
# for num in range(1, 10000001):
#     for value in range(num):
#         remainder = num % value
#         remainder_list.append(remainder)
#
#     if 0 in remainder_list == False:
#         < u > print(num) < / u >
# < / body >
# < / html >
