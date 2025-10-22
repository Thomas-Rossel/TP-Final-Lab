import random #para el queue (crear pedidos aleatorios)

class Hash:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)] #se crea la lista de listas

    #obtener su index
    def hash_function(self, value):
        value_str = str(value)
        return sum(ord(char) for char in value_str) % self.size


    #añadir el valor
    def add(self, value):
        index = self.hash_function(str(value))
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    #ver si un valor esta
    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    #remover valor
    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    #mostrar valor
    def show(self):
        print("Contenidos del Hash:")
        for index, bucket in enumerate(self.buckets):
            print(f"Espacio {index}: {[str(name) for name in bucket]}")

    #reemplazar valores
    def modify(self, old_value, new_value):
        index = self.hash_function(old_value)
        bucket = self.buckets[index]
        try:
            idx_in_bucket = bucket.index(old_value)
            bucket[idx_in_bucket] = new_value
            print(f"'{old_value}' modificado a '{new_value}'")
        except ValueError:
            print(f"No se encontro el siguiente valor:'{old_value}'")

    #funcion para crear una lista que luego va a ser usada con el queue, contiene todos los productos
    def products(self):
        books = []
        for index in self.buckets:
            for bucket in index:
                if bool(bucket):
                    books.append(bucket)
        return books

class Book:
    
    def __init__(self, name, price, stock, gender):
        self.name = name
        self.price = price
        self.stock = stock
        self.gender = gender
    
    def __str__(self):
        return f"{self.name}"
    
    def modify_atribute(self, atribute, new_value):
        setattr(self, atribute, new_value)
    
hash = Hash()

eternauta = Book('eternauta', 35000, 'si', 'Horror Cosmico')
the_sandman = Book('the_sandman', 24000, 'no', 'Mitologia')
x_men = Book('x_men', 50000, 'no', 'Superhéroes')
watchmen = Book('watchmen', 20000, 'si', 'Drama')
the_walking_dead = Book('the_walking_dead', 30000, 'si', 'Zombies')


hash.add(eternauta)
hash.add(the_sandman)
hash.add(x_men)
hash.add(watchmen)
hash.add(the_walking_dead)

hash.show()

#-------------------------------------------------------------------------------------------------------------------------

import random

class Queue:

    def __init__(self):
        self.queue = []
        self.products = hash.products()
        self.customers = ['Adrian', 'Santiago', 'Facundo', 'Luciano', 'Gustavo']

    def order(self):
        product = random.choice(self.products)
        customer = random.choice(self.customers)
        while product.stock == 'no':
            print(f'lo lamento señor {customer} pero {product} no esta a la venta ahora mismo')
            product = random.choice(self.products)
        order = (product, customer)
        return order

    def enqueue(self):
        order_ = self.order()
        self.queue.append(order_)
        print(f'Se añadio el pedido de "{order_[0]}", perteneciente a {order_[1]}, a la lista de espera')

    def dequeue(self):
        if bool(self.queue):
            element = self.queue.pop(0)
            print(f'{element[1]} ya fue atendido y recibio su libro "{element[0]}"')
        else:
            print('la lista ya esta vacia')

    def peek(self):
        if not bool(self.queue):
            self.isempty()
        else:
            frontElement = self.queue[0]
            print("El proximo en ser atendido sera:", frontElement[1])

    def isempty(self):
        if not bool(self.queue):
            print('No queda nadie por ser atendido')

    def size(self):
        print("El largo de la fila es de: ", len(self.queue))

queue = Queue()

queue.enqueue()
queue.enqueue()
queue.enqueue()
queue.dequeue()
queue.peek()
queue.isempty()
queue.size()

#-------------------------------------------------------------------------------------------------------------------------

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)