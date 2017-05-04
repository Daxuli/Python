"""
https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/040-SymPy-Intro.ipynb

https://github.com/AeroPython/Curso_AeroPython/blob/master/notebooks_completos/040-SymPy-Mecanica.ipynb

Calculo simbolico con SymPy
"""
from sympy import *
import sympy

init_printing()
# init_session()

x, y, z1, t = symbols('x y z t')  # p.e. si imprimimos z1 va a salir el simbolo z
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

print(2*z1)
print("-------------------------------------")

print(sympy.Integral(sqrt(1/x), x))
print(latex(Integral(sqrt(1/x), x)))  # para meter en LaTeX, que no tengo instalado
print(pretty(Integral(sqrt(1/x), x), use_unicode=False))
print("-------------------------------------")

print(latex(integrate(sqrt(1/x), x)))  # la solucion
print(pretty(integrate(sqrt(1/x), x)))
print("-------------------------------------")

expr = cos(x)**2 + sin(x)**2
print(expr)
print(simplify(expr))  # simplifica expresion
print(expr.subs(cos(x), y))  # sustituye cos(x) por y
