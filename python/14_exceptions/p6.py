class MyCustomException(Exception):
    def __init__(self, message="This is a custom exception."):
        self.message = message
        super().__init__(self.message)

# Raise the custom exception with your own message
raise MyCustomException("This is a custom exception with my own message.")
