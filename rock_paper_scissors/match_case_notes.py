# ------------------------------------------------------------------
# A case statement can only hold patterns, and

# **********variables aren't patterns.*************

# So, the approach below does not work.
# Somehow the line 'case y' causes y to be assigned
# to the value of x, which causes the error of
# 'irrefutable pattern':
# "Irrefutable pattern is allowed only for the last case statement

# x = input()
# y = input()
# z = input()
# match x:
#     case y:
#         print("something")
#     case z:
#         print("anything")

# However, turning these variables into class attributes
# makes them patterns, which solves the problem.
class Vars:
    x = int(input())
    y = int(input())
    z = int(input())
match Vars.x:
    case Vars.y:
        print("something")
    case Vars.z:
        print("anything")

# Or using if statements on at least one case
x = input()
y = input()
z = input()
match x:
    case y if y == 1:
        print("something")
    case z:
        print("anything")

# inline 'if' statement
a = 1
b = 0
match a:
    case 1 if b < 1:
        print('ok ok')


# ------------------------------------------------------------------
# LOGICAL OPERATORS

# The only acceptable (at least so far) is the 'or'(|) operator.
# Python's traditional 'or' statement won't work, however. 
#****** It has to be the 'or' logical sign, the 'pipe': | ******
a = 1
match a:
    case 1|2:
        print('ok')
# output: ok


# ------------------------------------------------------------------
# Class instances can be used as cases.
# Also, lists of instances.
# Examples from Python's docs:
class Point:
    x: int
    y: int

points = [Point(),Point()]

def location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on the x-axis.")
        case Point():
            print("The point is located somewhere else on the plane.")
        case _:
            print("Not a point")

match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point {x}, {y} is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
    case _:
        print("Something else is found in the list.")
# ------------------------------------------------------------------
# TUPLES
point = tuple()

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# ------------------------------------------------------------------
# Wildcard inside tuple:
# Example from Python's doc
test_variable = None

match test_variable:
    case ('warning', code, 40):
        print("A warning has been received.")
    case ('error', code, _):
        print(f"An error {code} occurred.")

# ------------------------------------------------------------------
# <This is a WRONG use of match/case!>

# If you put a variable in the case statement
# this variable will be assigned to the value of 
# the variable from the match statement
a = 9
b = 2
match a:
    case b:             # here b is assinged to 9.
        print('oook')   # so this line is executed



