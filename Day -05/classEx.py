class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(type(v).__name__)
print(v.__class__.__name__)