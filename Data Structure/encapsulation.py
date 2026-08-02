class SecretAgent:
    def __init__(self,name,code_name,password):
        self.name = name
        self._code_name = code_name
        self.__password = password

    def public(self):
        return f"hello {self.name}"

    def private(self):
        return f"yes {self._code_name}"

    def protected(self):
        return f"shhh {self.__password}"

Agent01 = SecretAgent('Bena','B370','007')
passw = Agent01.name
passw


sentence = "Python is fun to learn"


