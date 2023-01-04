import re
# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be: john
# In case of input data being supplied to the question, it should be assumed to be a console input.


class NameFinder:
    def __init__(self):
        self.email = input("Enter your email here : ")

    def validate_email(self):
        self.email_regex = re.compile(
            pattern=r"([A-Za-z]+)(@)([A-Za-z]+)(\.com)")
        if self.email_regex.match(self.email):
            return True
        else:
            return False

    def name_xtractor(self):
        if self.validate_email():
            name = self.email_regex.search(self.email).group(1)
            print(f"Name = {name}")
        else:
            print("Invalid Email")


name = NameFinder()
name.name_xtractor()
