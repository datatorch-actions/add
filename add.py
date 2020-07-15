import sys
import datatorch

if __name__ == "__main__":
    inputs = datatorch.get_inputs()
    x: int = inputs.get('x')
    y: int = inputs.get('y')
    for i in range(x+y):
        print(i)
    datatorch.set_output('s', x + y)
