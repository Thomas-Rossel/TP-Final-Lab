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

queue = []

products = hash.products()
customers = ['Adrian', 'Santiago', 'Facundo', 'Luciano', 'Gustavo']

#funcion para simular una orden aleatoria
def order():
    product = random.choice(products)
    customer = random.choice(customers)
    while product.stock == 'no':
        print(f'lo lamento señor {customer} pero {product} no esta a la venta ahora mismo')
        product = random.choice(products)
    order = (product, customer)
    return order
   


def enqueue():
    order_ = order()
    queue.append(order_)
    print(f'Se añadio el pedido de "{order_[0]}", perteneciente a {order_[1]}, a la lista de espera')

def dequeue():
    if bool(queue):
        element = queue.pop(0)
        print(f'{element[1]} ya fue atendido y recibio su libro "{element[0]}"')
    else:
        print('la lista ya esta vacia')

def peek():
    frontElement = queue[0]
    print("El proximo en ser atendido sera:", frontElement[1])


def isempty():
    if not bool(queue):
        print('No queda nadie por ser atendido')

def size():
    print("El largo de la fila es de: ", len(queue))

enqueue()
enqueue()
enqueue()
enqueue()
dequeue()
peek()
dequeue()
size()
isempty()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
size()