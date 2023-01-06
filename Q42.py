# Write a function to compute 5/0 and use try/except to catch the exceptions.

def divider():
    return 5/0


try:
    divider()
except ZeroDivisionError as e:
    print(f"error occurred - {e}")
else:
    print("Division Successful")
finally:
    print("Testing division")
