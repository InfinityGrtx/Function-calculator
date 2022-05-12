
# function calculator

the function calculator can easily calculate different formulas.
![math-capable](https://user-images.githubusercontent.com/102982291/168146395-6d8bb04f-a43e-4ee2-8981-1e44c48ddcac.svg)

[colab](https://colab.research.google.com/github/InfinityGrtx/Function-calculator/blob/main/Jupyter%20notebook/function_calculator%20(1).ipynb)

# availiable functions

currently, you could use:
- pythagorean theorem

- inverse pythagorean theorem

- intersecting chords

- intersecting secants

- intersecting tangent and chord

- pyramid volume


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
- a web application
- a larger database of formulas (possibly seperate)
- 
