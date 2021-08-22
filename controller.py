class Controller():

    def __init__(self, functions):
        self.functions = functions
        self.__done = False

    @property
    def done(self):
        return self.__done

    @done.setter
    def done(self, value):
        if value is True or value is False:
            self.__done = value
        else:
            raise ValueError(f'Could not assign {value} to done (only True or False)')

    def run_function(self, command):
        function = self.functions.get(command)
        if function is not None:
            function()
            return True
        return False

    def display_tasks(self):
        return "All task's names:\n" + '\n'.join(self.functions.keys())
