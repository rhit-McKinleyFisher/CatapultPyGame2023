import random


def variables():
    print('Variables')
    ex_int = 7
    print(type(ex_int))
    ex_str = 'mckinley'
    print(type(ex_str))
    ex_bool = True
    print(type(ex_bool))
    ex_list = [1, 30]
    print(type(ex_list))


def flow_control():
    print('Flow control')
    # If statements
    x = random.randint(1, 1111)
    print(x)
    if x < 100:
        print('x is small')
    elif x == 1000:
        print('x is one thousand')
    elif x == 200 or x == 300:
        print('x is 200 or 300')
    else:
        print('X is big')

    # Loops
    for k in range(5):
        print(k)

    print(type(range(5)))
    my_scores = [95, 82, 37, 100]
    print(my_scores[3])

    for score in my_scores:
        print('Loop:', score)


def functions(a, b, c):
    print('I got', a, b, c)
    return (a + b) * c


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


def making_classes():
    print('Classes')
    pt1 = Point(3, 5)
    print(pt1.x, pt1.y)
    pt1.x += 10
    print(pt1.x, pt1.y)

    pt2 = Point(100, 500)
    pt2.move(3, 7)
    print(pt2.x, pt2.y)


def main():
    print("Speaking Python")
    # variables()
    # flow_control()
    # x = functions(1, 3, 56)
    # y = functions(89, 3, -2)
    # print(x, y)
    # making_classes()


main()
