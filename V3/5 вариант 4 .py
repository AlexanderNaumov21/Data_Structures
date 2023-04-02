#Вариант4
class Ctek: 
	__ctek_cpicok = [] 
	def __init__ (self): 
		pass
	def dobavlenie (self, x): 
		self.x = x
		self.__ctek_cpicok.append(x)
	def vivod(self): 
		print("Последний, введенный в стек, элемент - ",self.__ctek_cpicok[-1]," выведен из стека.")
		q = self.__ctek_cpicok.pop(-1) 
		return q
	def infoctek(self):
		print("Наш стек - ",self.__ctek_cpicok)


e = Ctek()
arr = [-99, 55,9,-5,-66,-51,1,2,64] 
for i in arr: 
	e.dobavlenie(i)
e.infoctek()
print("Введем 333")
e.dobavlenie(333)
e.infoctek()
print("Выведем последний элемент")
e.vivod()
e.infoctek()

