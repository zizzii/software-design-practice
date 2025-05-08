import math


# class Shape:
#     def __init__(self, name):
#         self.name = name
#     def perimeter(self):
#         raise NotImplementedError("perimeter")
#     def area(self):
#         raise NotImplementedError("area")

# class Square(Shape):
#     def __init__(self,name,side):
#         super().__init__(name)
#         self.side = side
#     def perimeter(self):
#         return self.side * 4
#     def area(self):
#         return self.side ** 2
    
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
#     def perimeter(self):
#         return self.radius * 2 * math.pi
#     def area(self):
#         return self.radius ** 2 * math.pi


def make(cls, *args):
    return cls["_new"](*args)

def shape_new(name):
    return {
        "name" : name,
        "_classname": Shape
    }

def density(thing, weight):
    return weight / call(thing, "area")

Shape = {
    "_classname": "Shape",
    "density": density,
    "_parent" : None,
    "_new": shape_new
}
def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

def square_larger(thing, size):
    return call(thing, "area") > size

def square_new(name, side):
    return make(Shape, name) | {
        "side": side,
        "_class": Square,
    }

Square = {
    "perimeter" : square_perimeter,
    "area": square_area,
    "_classname": "Square",
    "_parent": Shape,
    "_new": square_new
}


def circle_larger(thing, size):
    return call(thing, "area") > size

def circle_perimeter(thing):
    return thing["side"] * 2 * math.pi

def circle_area(thing):
    return thing["side"] ** 2 * math.pi

Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "_classname": "Circle",
    "_parent": Shape
}

def circle_new(name, side):
    return {
        "name" : name,
        "side": side,
        "larger": circle_larger,
        "_class": Circle,
    }

def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    return NotImplementedError("method_name")

#Apply the method name from class 'thing' to the class 'thing'
def call(thing, method_name, *args, **kwargs):
    method = find(thing["_class"], method_name)
    #return thing["_class"][method_name](thing, *args)
    return method(thing, *args, **kwargs)


if __name__ == "__main__":
    examples = [make(Square, "sq", 3),]
    for ex in examples:
        n = ex["name"]
        d = call(ex, "density", 5)
        print(f'The density of {n}: {d:.2f}')