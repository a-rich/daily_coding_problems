def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(f):
    def first(a,b):
        return a
    return f(first)

def cdr(f):
    def last(a,b):
        return b
    return f(last)

if __name__ == '__main__':
    print(car(cons(3,4)))
    print(cdr(cons(3,4)))
