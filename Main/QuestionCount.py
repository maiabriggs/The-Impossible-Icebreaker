count = 2

def decrease():
    global count
    count -= 1

def checkCount():
    if count == 0:
        return False
    else:
        return True

