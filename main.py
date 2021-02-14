X = 0
Y = 0
C = 0
D = 0

def on_forever():
    global X, Y, C, D
    X = randint(1, 10)
    Y = randint(1, 10)
    C = X * Y
    D = Math.constrain(C, 1, 30)
    if C <= 30:
        basic.show_number(X)
        basic.pause(2000)
        basic.show_string("X")
        basic.pause(1500)
        basic.show_number(Y)
        basic.pause(2000)
    else:
        pass
basic.forever(on_forever)
