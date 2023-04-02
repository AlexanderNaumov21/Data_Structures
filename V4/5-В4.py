import random
#Вариант4
class Stec: 
	__stecArray = [] 
	def set (self, p): 
		self.p = p
		self.__stecArray.append(p)
	def get(self): 
		print("Крайний элемент выведен из стека и передан на переменную.")
		w = self.__stecArray.pop(-1) 
		return w
	def get_inform(self):
		print("Стек сейчас выглядит так:",self.__stecArray)

e = Stec()
array1 = [] 
for i in range(8):
	p = random.randint(-100, 100)
	array1.append(p)
for i in array1: 
	e.set(i)

e.get_inform()
print("Введем 4")
e.set(4)
e.get_inform()
print("Выведем крайний элемент")
y = e.get()
print("Крайней элемент, выведенный на переменную у: ", y)
e.get_inform()