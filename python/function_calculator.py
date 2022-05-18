import math
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
def paragariumtheorem(a, b):
  a2 = pow(a, 2)
  b2 = pow(b, 2)
  c2 = a2 + b2
  c = math.sqrt(c2)
  print('your answer is %d' % c)

def inversepythagoreantheorem(a, c):
  a2 = pow(a, 2)
  c2 = pow(c, 2)
  b2 = c2 - a2
  b = math.sqrt(b2)
  print('Your answer is %d' % b)

def findintersectingchords(x,y):
  z = x + y
  answer = z / 2
  print('Your answer is %d' % answer)

def findintersectingsecants(x,y):
  z = x - y
  answer = z / 2
  print('your answer is %d' % answer)

def findintersectingtangethord(x):
  y = x / 2
  print('your answer is %d' % y)

def pyramidvolume(b, h):
  answer = b*h / 3
  print('your answer is %d' % answer)

def translation(x,y,x1,y1):
  newx = x + x1
  newy = y + y1
  print("your new x is %d" % newx)
  print("your new y is %d" % newy)

def dilation(k,x,y):
  newx = x * k
  newy = y * k
  print('your new x is %d' % newx)
  print('your new y is %d' % newy)

def circlearea(r, pi):
  r2 = pow(r,2)
  answer = pi * r2
  print('your answer is %d' % answer)

def findscalefacter(l1,l2):
  answer = l1/l2
  print('your answer is %d' % answer)

def setupformula(formula):
  if formula == '1': 
    a = float(input('first value: '))
    b = float(input('second value: '))
    paragariumtheorem(a, b)
  elif formula == '2':
    a = float(input('known leg value: '))
    c = float(input('Hypotenuse value: '))
    inversepythagoreantheorem(a, c)
  elif formula == '3':
    x = float(input('value of arc one: '))
    y = float(input('value of arc two: '))
    findintersectingchords(x,y)
  elif formula == '4':
    x = float(input('value of arc one: '))
    y = float(input('value of arc two: '))
    findintersectingsecants(x,y)
  elif formula == '5':
    x = float(input('value of arc: '))
    findintersectingtangethord(x)
  elif formula == '6':
    b = float(input('the area of the base is: '))
    h = float(input('the hight of the pyramid is: '))
    pyramidvolume(b, h)
  elif formula == '7':
    x = float(input('the original x value is: '))
    y = float(input('the original y value is: '))
    x1 = float(input('how much to translate on the x axis: '))
    x2 = float(input('how much to translate on the y axis: '))
    translation(x,y,x1,x2)
  elif formula == '8':
    x = float(input('the original x value is: '))
    y = float(input('the original y value is: '))
    k = float(input('the scale factor is: '))
    dilation(k,x,y)
  elif formula == '9':
    r = float(input('the radius of the circle is: '))
    circlearea(r,pi)
  elif formula == '10':
    l1 = float(input('side length of shape A: '))
    l2 = float(input('side length of shape B: '))
    findscalefacter(l1,l2)
  else:
    print('Formula unknown')

"""# Availiable functions
- pythagorean theorem (function id: 1)

- inverse pythagorean theorem (function id: 2)

- intersecting chords (function id: 3)

- intersecting secants (function id: 4)

- intersecting tangent and chord (function id: 5)

- pyramid volume (function id: 6)

- translation (function id: 7)

- dilation (function id: 8)

- circle area (function id: 9)

- find scale factor (function id: 10)
"""

formula = input('enter function id: ')
setupformula(formula)