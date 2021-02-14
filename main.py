D = 0
X = 0
Y = 0
C = 0

def on_button_pressed_a():
    global D
    D += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global X, Y, C, D
    X = randint(1, 10)
    Y = randint(1, 10)
    C = X * Y
    D = 0
    while C <= 30:
        basic.show_number(X)
        basic.pause(2000)
        basic.show_string("*")
        basic.pause(1500)
        basic.show_number(Y)
        basic.pause(2000)
        basic.clear_screen()
        basic.show_string("?")
        basic.pause(2000)
basic.forever(on_forever)
