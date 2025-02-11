class Employee:
    def __init__(self, role , dept , sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def showDetails(self):
            print("role=",self.role)
            print("dept=",self.dept)
            print("sal=",self.sal)

class Engineer(Employee):
     def __init__(self, name , age):
          self.name=name
          self.age=age
          super().__init__("accountant","finance","60,000")


e1=Engineer("elon  musk","25")
e1.showDetails()