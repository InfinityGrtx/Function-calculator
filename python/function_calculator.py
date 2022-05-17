import math
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
def paragariumtheorem(a, b):
  a2 = pow(a, 2)
  b2 = pow(b, 2)
  c2 = a2 + b2
  c = math.sqrt(c2)
  print('your answer is: ')
  print(c)

def inversepythagoreantheorem(a, c):
  a2 = pow(a, 2)
  c2 = pow(c, 2)
  b2 = c2 - a2
  b = math.sqrt(b2)
  print('Your answer is: ')
  print(b)

def findintersectingchords(x,y):
  z = x + y
  answer = z / 2
  print(answer)

def findintersectingsecants(x,y):
  z = x - y
  answer = z / 2
  print(answer)

def findintersectingtangethord(x):
  y = x / 2
  print(y)

def pyramidvolume(b, h):
  answer = b*h / 3
  print('your answer is: ')
  print(answer)

def translation(x,y,x1,y1):
  newx = x + x1
  newy = y + y1
  print("your new x is: ")
  print(newx)
  print("your new y is: ")
  print(newy)

def dilation(k,x,y):
  newx = x * k
  newy = y * k
  print('your new x is: ')
  print(newx)
  print('your new y is: ')
  print(newy)

def circlearea(r, pi):
  r2 = pow(r,2)
  answer = pi * r2
  print('your answer is')
  print(answer)

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
  else:
    print('Formula unknown')

print('availiable functions are: 1: Pythagorean theorem, 2: Inverse Pythagorean theorem. 3: find intersecting chords, 4: find intersecting secants. 5: find intersecting tangent and chord. 6: pyramid volume. 7: 2d translation, 8: dilation. 9: circle area')
formula = input('enter function: ')
setupformula(formula)