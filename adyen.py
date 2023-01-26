# Complete the Message class that processes messages between sender and receiver.

# 1. Initialize the class variables with the values passed by the constructor.
# 2. When print(MessageObject) is called, only the message should be printed and only the message should be returned when str(MessageObject) is called
# 3. When comparing two Message objects, only their message attribute should be considered, True if they are equal and False if they are not.

# Fore example,
# message1 = Message("Hello!", 1,2)
# message2 = Message("Hello World!", 3,2)
# message3 = Message("Hello World!", 1,3)
# print(message1) # Hello!
# message1 == message2 # False
# message2 == message3 # True

# Constraints
# Maximum number of messages = 50
# Maximum number of print/eq querries = 50
# Maximum message length = 100 words
# Sender and Receiver id are integers between 0 and 100


class Message:
    def __init__(self, message, sender, receiver):
        self.message = message
        self.sender = sender
        self.receiver = receiver

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message

    def __eq__(self, other):
        if isinstance(other, Message):
            return self.message == other.message
        return False


message1 = Message("Hello!", 1, 2)
message2 = Message("Hello World!", 3, 2)
message3 = Message("Hello World!", 1, 3)

print(message1)  # Hello!

print(message1 == message2)  # False
print(message2 == message3)  # True
