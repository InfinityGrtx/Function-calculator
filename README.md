
# function calculator

the function calculator can easily calculate different formulas.

![math-capable](https://user-images.githubusercontent.com/102982291/168146395-6d8bb04f-a43e-4ee2-8981-1e44c48ddcac.svg)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-reason.svg)](https://forthebadge.com)
![made-from-boredom](https://user-images.githubusercontent.com/102982291/168147675-a5629063-081c-4a36-aadc-6d3afd120aac.svg)
[![forthebadge](https://forthebadge.com/images/badges/contains-tasty-spaghetti-code.svg)](https://forthebadge.com)

[colab](https://colab.research.google.com/github/InfinityGrtx/Function-calculator/blob/main/Jupyter%20notebook/function_calculator.ipynb)

# availiable functions

currently, you could use:
- pythagorean theorem (function id: 1)

- inverse pythagorean theorem (function id: 2)

- intersecting chords (function id: 3)

- intersecting secants (function id: 4)

- intersecting tangent and chord (function id: 5)

- pyramid volume (function id: 6)

- translation (function id: 7)

- dilation (function id: 8)

- circle area (function id: 9)


# adding a function

to add a function, you first have to define the function. to do this, you need to define how to solve the problem using floats. example:
                def addtwo(x):
                  answer = x + 2
                  print(answer)

 then, you have to add an elif that activates when the user inputs the formula. in the elif, you would include code that sets the floats used in the function, this is done with the input function. example:
        x = float(input('value of x: ')).
   then in the elif, you need to call the function you defined by doing addtwo(x). 

   then add the function name to the end of the print function that lists the function, give it the next availiable number. the number would be what the if function calls


# future plans
the function calculator currently is more bare bones, and a first python project. 
- a larger database of formulas (possibly seperate)
- possible web interface
