class Queue_list: #создаем класс очереди
	__list1 = [] # создаем защищенный от изменений список (__ - не позволяют вызвать, изменять значения снаружи)
	def __init__ (self): # конструктор
		pass

	def Addendum (self, elem): # задаем метод добавления элемента в очередь
		self.elem = elem
		self.__list1.append(elem)

	def Appeal_first(self): # задаем метод вывода первого элемента из очереди
		print(f"Первый элемент в очереди: {self.__list1[0]}, пошел в обработку.")
		return self.__list1[0]
		self.__list1.pop(0)
		
	def info_first(self): # метод вывода информация по первому элементу
		print(f"Первый элемент:{self.__list1[0]}")
	def info_finish(self):# метод вывода информация по последниму элементу
		print(f"Последний элемент:{self.__list1[-1]}")

w = Queue_list()		# создаем экземпляр
list2 = [1,2,3,4,5,6,7,8,9] # задаем список 
for i in list2: # добавляем его в очередь через цикл
	w.Addendum(i)
w.info_first()
w.info_finish()	
print("Dobavlenie")
w.Addendum(10) # добавляем "10" в нашу очередь
w.info_first()
w.info_finish()
print("ydalenie pervogo")
z = w.Appeal_first() # принимаем объект из очереди
print("Переданный нам объект из очереди:",z)
w.info_first()
w.info_finish()
print(w.__list1[2]) # ошибка в этой строчки доказывает что мы не можем узнать другие элементы из очереди