def make_pretty(func):#func=ordinary
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty#ordinary = make_pretty(ordinary)
def ordinary():
    print("I am ordinary")
ordinary()#inner()
