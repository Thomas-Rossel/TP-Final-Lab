class Hash:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        value_str = str(value)
        return sum(ord(char) for char in value_str) % self.size

    def add(self, value):
        value_str = str(value)
        index = self.hash_function(value_str)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value_str)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def show(self):
        print("Contenidos del Hash:")
        for index, bucket in enumerate(self.buckets):
            print(f"Espacio {index}: {bucket}")

    def modify(self, old_value, new_value):
        index = self.hash_function(old_value)
        bucket = self.buckets[index]
        try:
            idx_in_bucket = bucket.index(old_value)
            bucket[idx_in_bucket] = new_value
            print(f"'{old_value}' modificado a '{new_value}'")
        except ValueError:
            print(f"No se encontro el siguiente valor:'{old_value}'")

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