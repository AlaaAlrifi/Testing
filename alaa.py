class Person :
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def prit_First_name(self):
        print(self.first_name)

    def prit_Last_name(self):
        print(self.last_name)
alaa=Person("alaa","ihsan")
alaa.prit_First_name()
alaa.prit_Last_name()