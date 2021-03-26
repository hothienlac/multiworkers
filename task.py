

# FUNCTION AND CALLBACK ACCEPT ONLY ONE ARGUMENT
class Task:

    def __init__(self, function, argument, callback):
        self.function       = function
        self.argument       = argument
        self.callback       = callback


    def run(self):
        result = self.function(self.argument)
        self.callback(result)
