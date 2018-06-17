
class Animal():
	def __init__(self,name,id):
		self.name=name
		self.id=id
	def getId(self):
		return self.id
	def setId(self,id):
		self.id=id

dog = Animal('dog',1)
id = dog.getId()
print(id)
dog.setId(2)
id = dog.getId()
print(id)

