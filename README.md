
# function calculator

the function calculator can easily calculate different formulas.

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
