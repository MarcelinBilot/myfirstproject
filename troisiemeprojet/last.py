
def add(a):
    a += 1
    print(a)

    if a < 10:
        add(a)


add(2)