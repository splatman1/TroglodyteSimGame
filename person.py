class Person:
    def __init__(self, location=None):
        self.is_dead = False
        self.location = location
        while True:
            if self.is_dead:
                print("Dead")

