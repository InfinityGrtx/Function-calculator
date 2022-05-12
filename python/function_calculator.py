import math

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
    
  else:
    print('Formula unknown')

print('availiable functions are: 1: Pythagorean theorem, 2: Inverse Pythagorean theorem. 3: find intersecting chords, 4: find intersecting secants. 5: find intersecting tangent and chord. 6: pyramid volume')

formula = input('enter function: ')
setupformula(formula)
