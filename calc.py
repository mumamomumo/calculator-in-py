eq = str(input('Type a basic expression (addition (+), substraction(-), multiplication(*), division(/)) '))
try: eval(eq)
except NameError or SyntaxError: print('Idjot')
else:print(eval(eq))