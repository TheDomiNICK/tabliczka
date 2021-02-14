let X = 0
let Y = 0
let C = 0
let D = 0
basic.forever(function () {
    X = randint(1, 10)
    Y = randint(1, 10)
    C = X * Y
    D = Math.constrain(C, 1, 30)
    if (C <= 30) {
        basic.showNumber(X)
        basic.pause(2000)
        basic.showString("X")
        basic.pause(1500)
        basic.showNumber(Y)
        basic.pause(2000)
    } else {
    	
    }
})
