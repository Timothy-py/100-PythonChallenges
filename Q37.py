# Define a class named American and its subclass NewYorker.

class American:
    def __init__(self):
        pass


class NewYorker(American):
    def __init__(self):
        super.__init__(American)
