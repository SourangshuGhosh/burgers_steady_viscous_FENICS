#! /usr/bin/env python3
#
from dolfin import *

def burgers_steady_viscous ( e_num, nu ):

#*****************************************************************************80
#
## burgers_steady_viscous solves the steady viscous 1D Burgers equation.
#
#  Discussion:
#
#    -nu u'' + u del u = 0, -1 < x < 1
#    u(-1) = -1, u(1) = 1
#
#    This equation is nonlinear in U.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    By Sourangshu Ghosh
#
#  Author:
#
#    Sourangshu Ghosh
#
#  Parameters:
#
#    Input, integer E_NUM, the number of elements to use.
#
#    Input, real NU, the viscosity.
#    NU should be positive.  The larger it is, the smoother the solution.
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'burgers_steady_viscous:' )
  print ( '  FENICS/Python version' )
  print ( '  Number of elements is %d' % ( e_num ) )
  print ( '  Viscosity set to %g' % ( nu ) )
#
#  Create a mesh on the interval [-1,+1].
#
  x_left = -1.0
  x_right = +1.0
  mesh = IntervalMesh ( e_num, x_left, x_right )
#
#  Define the function space to be of Lagrange type
#  using piecewise linear basis functions.
#
  V = FunctionSpace ( mesh, "CG", 1 )
#
#  Define the boundary conditions.
#  if X <= XLEFT + eps, then U = U_LEFT
#  if X_RIGHT - eps <= X, then U = U_RIGHT
#
  u_left = -1.0
  def on_left ( x, on_boundary ):
    return ( x[0] <= x_left + DOLFIN_EPS )
  bc_left = DirichletBC ( V, u_left, on_left )

  u_right = +1.0
  def on_right ( x, on_boundary ):
    return ( x_right - DOLFIN_EPS <= x[0] )
  bc_right = DirichletBC ( V, u_right, on_right )

  bc = [ bc_left, bc_right ]
#
#  Define the trial functions (u) and test functions (v).
#
  u = Function ( V )
  v = TestFunction ( V )
#
#  Write the function F.
#
#  What I wanted to write:
#
#    F = ( nu * inner ( grad ( u ), grad ( v ) ) + inner ( u * grad ( u ), v ) ) * dx
#
#  What I ended up writing:
#
  F = \
  ( \
    nu * inner ( grad ( u ), grad ( v ) ) \
  + inner ( u * u.dx(0), v ) \
  ) * dx
#
#  Specify the jacobian.
#
  J = derivative ( F, u )
#
#  We use a form of the solve command that recognizes that we are
#  working with a nonlinear equation.
#
  solve ( F == 0, u, bc, J = J )
#
#  Plot the solution.
#
  plot ( u, title = 'burgers steady viscous equation' )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- U(X) --->' )
  filename = 'burgers_steady_viscous.png'
  plt.savefig ( filename )
  print ( 'Graphics saved as "%s"' % ( filename ) )
  plt.close ( )

  return

def burgers_steady_viscous_test ( ):

#*****************************************************************************80
#
## burgers_steady_viscous_test tests burgers_steady_viscous.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    by Sourangshu Ghosh
#
#  Author:
#
#    Sourangshu Ghosh
#
  import dolfin
  import platform
#
#  Report level = only warnings or higher.
#
  level = 30
  set_log_level ( level )

  print ( '' )
  print ( 'burgers_steady_viscous_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FENICS version %s'% ( dolfin.__version__ ) )
  print ( '  Solve the steady 1d Burgers equation.' )

  e_num = 16
  nu = 0.1
  burgers_steady_viscous ( e_num, nu )
#
#  Terminate.
#
  print ( "" )
  print ( "burgers_steady_viscous_test:" )
  print ( "  Normal end of execution." )

  return

if ( __name__ == '__main__' ):
  import time
  print ( time.ctime ( time.time() ) )
  burgers_steady_viscous_test ( )
  print ( time.ctime ( time.time() ) )
