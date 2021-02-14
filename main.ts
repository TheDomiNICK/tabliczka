let D = 0
let X = 0
let Y = 0
let C = 0
input.onButtonPressed(Button.A, function () {
    D += 1
})
basic.forever(function () {
    X = randint(1, 10)
    Y = randint(1, 10)
    C = X * Y
    D = 0
    while (C <= 30) {
        basic.showNumber(X)
        basic.pause(2000)
        basic.showString("*")
        basic.pause(1500)
        basic.showNumber(Y)
        basic.pause(2000)
        basic.clearScreen()
        basic.showString("?")
        basic.pause(2000)
    }
})
