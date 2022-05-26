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

def rectangleprismarea(l,w,h):
  answer = l*w*h
  print('your answer is %d' % answer)

def rectangleprismsa(l,w,h):
  answer = 2 * l * w + 2 * l * h + 2 * w * h
  print('your answer is %d' % answer)

def pyramidsa(l,p,b):
  answer =  l*p
  answer = answer + b
  answer = answer / 2
  print('your answer is %d' % answer)

def cylindervolume(pi,r,h):
  r2 = pow(r,2)
  answer = pi*r2*h
  print('your anwser is %d' % answer)

def cylindersa(pi, r,h):
  r2 = pow(r,2)
  answer = 2 * pi * r2 + 2 * pi * r * h
  print('your answer is %d' % answer)

def triprismvolume(b,h):
  answer = b*h
  print('your answer is %d' % answer)

def triprismsa(h,p,b):
  answer = h*p+2*b
  print('your answer is %d' % answer)

def conevolume(pi,r,h):
  r2 = pow(r,2)
  answer = pi * r2 * h/3
  print("your answer is %d" % answer)

def conesa(pi, r, l):
  r2 = pow(r,2)
  answer = pi*r2 + pi * r*l
  print("your answer is %d" % answer)

def trianglearea(b,h):
  answer = b*h/2
  print("your answer is %d" % answer)

def rectanglearea(l,w):
  answer = l*w
  print("your answer is %d" % answer)

def rectangleperimiter(l,w):
  answer = 2*l+2*w
  print("your answer is %d" % answer)

def parallelagramarea(b,h):
  answer = b*h
  print("your answer is %d" % answer)

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
  elif formula == '11':
    l = float(input('the length is: '))
    w = float(input('the width is: '))
    h = float(input('the height is: '))
    rectangleprismarea(l,w,h)
  elif formula == '12':
    l = float(input('the length is: '))
    w = float(input('the width is: '))
    h = float(input('the height is: '))
    rectangleprismsa(l,w,h)
  elif formula == '13':
    l = float(input('the slant height is: '))
    p = float(input('the base parimiter is: '))
    b = float(input('the base area is: '))
    pyramidsa(l,p,b)
  elif formula == '14':
    r = float(input('the radius is: '))
    h = float(input('the height is: '))
    cylindervolume(pi,r,h)
  elif formula == '15':
    r = float(input('the radius is: '))
    h = float(input('the height is: '))
    cylindersa(pi,r,h)
  elif formula == '16':
    b = float(input('the area of the base is: '))
    h = float(input('the height is: '))
    triprismvolume(b,h)
  elif formula == '17':
    h = float(input('the height is: '))
    p = float(input(' the parimiter of the base is: '))
    b = float(input('the area of the base is: '))
    triprismsa(h,p,b)
  elif formula == '18':
    r = float(input('the radius is: '))
    h = float(input('the height is: '))
    conevolume(pi,r,h)
  elif formula == '19':
    r = float(input('the radius is: '))
    l = float(input('the slant height is: '))
    conesa(pi,r,l)
  elif formula == '20':
    b = float(input('the base is: '))
    h = float(input('the height is: '))
    trianglearea(b,h)
  elif formula == '21':
    l = float(input('the length is: '))
    w = float(input('the width is: '))
    rectanglearea(l,w)
  elif formula == '22':
    l = float(input('the length is: '))
    w = float(input('the width is: '))
    rectangleperimiter(l,w)
  elif formula == '23':
    b = float(input('the base is: '))
    h = float(input('the height is: '))
    parallelagramarea(b,h)
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

- find the volume of a rectangular prism (function id: 11)

- find the surface area of a rectangular prism (function id: 12)

- find the surface area of a pyramid (function id: 13)

- find the volume of a cylinder (function id: 14)

- find the surface area of a cylinder (function id: 15)

- find the volume of a triangular prism (function id: 16)

- find the surface area of a triangular prism (function id: 17)

- find the volume of a cone (function id: 18)

- find the surface area of a cone (function id: 19)

- find the area of a triangle (function id: 20)

- find the area of a rectangle (function id: 21)

- find the perimiter of a rectangle (function id: 22)

- find the area of a parallelagram (function id: 23)
"""

formula = input('enter function id: ')
setupformula(formula)
