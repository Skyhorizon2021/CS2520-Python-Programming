def f():
    global x
    x += 5
    y = 20
    def g():
        nonlocal y
        x = 20
        y += 10
    g()
    pri