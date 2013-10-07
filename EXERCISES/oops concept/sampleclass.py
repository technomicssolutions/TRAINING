class Employee:
    empCount = 0
    def _init_(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print "total employee %d" % Employee.empCount
    def displayEmployee(self):
        print "name : ",self.name, ",salary:",self.salary
emp1 = Employee("arun",2000)
emp2 = Employee("sharath",3000)
emp1.displayEmployee()
emp2.displayEmployee()
print "total employee %d" % Employee.empCount

