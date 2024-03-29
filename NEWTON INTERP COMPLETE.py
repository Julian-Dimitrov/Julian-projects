import matplotlib.pyplot as plt
import numpy as np

xs = []
y = []

print("!!!!! While adding numbers for decimal point use '.' !!!!!")
print("Enter x, y pairs:")

com = input()
while com != '':
    to_add = com.split(', ')
    xs.append(float(to_add[0]))
    y.append(float(to_add[1]))
    com = input()

print()
print("x value to calculate")

at_point = str(input())

print()
print("Graph? y/n")

graph = input()

# pravi list s prazni listove za vkarvane na stoinostite
all_DDPs = [[] for i in range(len(xs) - 1)]
all_DDPs.insert(0, y)


# pravi stoinostite i gi vkrava v listovete
for p in all_DDPs:
    for i in range(len(p) - 1):
        c = (p[i+1] - p[i]) / (xs[i + all_DDPs.index(p) + 1] - xs[i])
        all_DDPs[all_DDPs.index(p) + 1].append(c)


# vzima nuleviq element ot lista (koefficientite) i gi otdelq
coeffs = [i[0] for i in all_DDPs]


#postroqvane na polinoma i purvata mu prizvodna
polynomial = []
derivative = []

for i in range(len(coeffs)):
    l = []
    der = []
    for p in range(i):
        l.append('(' + 'x' + '-' + str(xs[p]) + ')')

    for k in range(len(l)):
        der.append('*'.join(l[:k] + l[k + 1:]))

    derivative.append([str(coeffs[i]) + '*' + p for p in der])
    polynomial.append(str(coeffs[i]) + '*' + "*".join(l))

polynomial[0] = str(y[0])
polynomial = " + ".join(polynomial)
print()
print("Polynomial function")
print(polynomial)
print()

derivative.pop(0)
derivative = [' + '.join(o) for o in derivative]
derivative[0] = str(coeffs[1])
derivative = ' + '.join(derivative)
print('Derivative')
print(derivative)
print()

# izchislqva funkciqta i proizvodnata v dadenata tochka ako ima takava
if type(at_point) == str and len(at_point) > 0:
    print(f"x = {at_point}")
    print(f"polynomial value {eval(polynomial.replace('x', at_point))}")
    print(f"derivative value {eval(derivative.replace('x', at_point))}")


# pravi intervalite na grafikata kato vzima 1/5 ot dulzhinata na x-ovete
abs_x = [abs(i) for i in xs]


# vzima 1000 ravnomerno razpredeleni stoinosti x v dadeniq interval, za da mozhe kompiutura da postroi grafikata po tqh
x = np.linspace(xs[0] - sum(abs_x) / 5, xs[-1] + sum(abs_x) / 5, 1000)


# dobavqne na nachalnite danni, postroqvane na grafikite na polinoma i proizvodnata mu

if graph == 'y':
    plt.scatter(xs, y, color='r', label="initial values")
    plt.plot(x, eval(polynomial), label="polynomial")
    plt.plot(x, eval(derivative), label="derivative")
    plt.legend(loc="best")
    plt.show()
