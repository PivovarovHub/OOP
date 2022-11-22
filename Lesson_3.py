'''
Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег,
которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.'''

class Money:
    def __init__(self, money = 0):
        self.money = money

my_money = Money(100)
your_money = Money(1000)

'''
Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), 
а третий необязательный аргумент - цвет точки (локальное свойство color). Если цвет не указывается, 
то он по умолчанию принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, 
с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку). 
Для второго объекта в списке points укажите цвет 'yellow'.

P.S. На экран в программе ничего выводить не нужно.
'''

class Point:
    
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = [Point(i, i) for i in range(1,2000,2)]
points[1] = Point(3, 3, 'yellow')

'''
Объявите три класса геометрических фигур: Line, Rect, Ellipse. 
Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов 
(произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp 
(верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно 
(или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения).
Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.
'''
from random import choice, sample

class Line:
    def __init__(self, a, b, c, d):
        self.sp, self.ep = (a, b), (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp, self.ep = (a, b), (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp, self.ep = (a, b), (c, d)


cls = (Line, Rect, Ellipse)

elements = [choice(cls)(*sample(range(10), 4)) for _ in range(217)]

for i in elements:
    if isinstance(i, Line):
        i.sp = i.ep = 0, 0

''' 
Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. 
Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
'''

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    def is_triangle(self):
        if not all(list(map(lambda x : type(x) in (int, float), (self.a, self.b, self.c)))):
            return 1
        elif any((self.a < 0, self.b < 0, self.c < 0)):
            return 1
        if not all([self.a + self.b > self.c, self.b + self.c > self.a, self.a + self.c > self.b]):
            return 2
        return 3

a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

'''
Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:

gr_1 = Graph(data)
где data - список из числовых данных (данные для графика). 
При создании каждого экземпляра класса должны формироваться следующие локальные свойства:

data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);

В этом классе объявите следующие методы:

set_data(self, data) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.

Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение:

"Отображение данных закрыто"

Прочитайте из входного потока числовые данные с помощью команды:

data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show() со значением fl_show = False и вызовите метод show_table(). 
На экране должны отобразиться две соответствующие строки.
'''

class Graph:
    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show
        
    def set_data(self, data):
        self.data = data
        
    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            self.close_acc()
            
    def show_graph(self):
        if self.is_show:
            print('Графическое отображеные данных:', *self.data)
        else:
            self.close_acc()
            
    def show_bar(self):
        if self.is_show:
            print('Столбчатая диаграмма:', *self.data)
        else:
            self.close_acc()
            
    def set_show(self, fl_show):
        self.is_show = fl_show

    def close_acc(self):
        print('Отображение данных закрыто')
        
        
# считывание списка из входного потока 
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()

'''
 Объявите в программе следующие несколько классов:

CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory,
 максимум N - по числу слотов памяти на материнской плате (N = 4).

Объекты классов должны иметь следующие локальные свойства: 

для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти 
(атрибут прописывается с этим значением и не меняется); 
mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате 
в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
'''


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        res = [f"Материнская плата: {self.name}",
               f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
               f"Слотов памяти: {self.total_mem_slots}",
               "Память: " + "; ".join([f"{x.name} - {x.volume}" for x in self.mem_slots])]
        return res


mb = MotherBoard("ASUS", CPU("RYZEN 5 3600", 4000), Memory('asus', 1333), Memory("aser", 1333))
mb.get_config()

'''. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup).
Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), 
два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами. 
'''

# здесь пишите программу
class Cart:
    
    def __init__(self, goods=[]):
        self.goods = goods
        
    def add(self, gd):
        self.goods.append(gd)
    
    def remove(self, idx):
        self.goods.pop(idx)

    def get_list(self):
        s = [f'{i.name}: {i.price}' for i in self.goods]
        return s
    
class Goods:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class TV(Goods):
    pass

class Table(Goods):
    pass

class Notebook(Goods):
    pass

class Cup(Goods):
    pass


cart = Cart()
tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)


'''Вам необходимо реализовать односвязный список из объектов класса ListObject


Для этого объявите в программе класс ListObject, объекты которого создаются командой:

obj = ListObject(data)
Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся строки из списка lst_in 
(первая строка в первом объекте, вторая - во втором и  т.д.).
На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.'''


import sys

# здесь объявляются все необходимые классы
class ListObject:
    
    def __init__(self, data):
        self.data = data
        self.next_obj = None
        
    def link(self, obj):
        self.next_obj = obj
        
        
# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять
# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new