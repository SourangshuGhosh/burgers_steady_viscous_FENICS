# burgers_steady_viscous
## FENICS Solution of the Steady Burgers Equation
burgers_steady_viscous, a FENICS code which uses the finite element method to solve a version of the steady viscous Burgers equation over the interval [-1,+1].

Note that I have installed FENICS using Docker, and so to run this script I issue the commands:

```html
cd $HOME/fenicsproject/burgers_steady_viscous
fenicsproject run
python3 burgers_steady_viscous.py
exit
```


## Reference:
Hans Petter Langtangen, Anders Logg,
Solving PDEs in Python - The FEniCS Tutorial Volume 1.

## Source Code:
burgers_steady_viscous.py a script which sets up and solves the problem.
burgers_steady_viscous.sh runs all the tests.
burgers_steady_viscous.txt the output file.
burgers_steady_viscous.png a plot of the solution.
