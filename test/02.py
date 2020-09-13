import  time

def logs():
    time_fomate = '%Y-%m-%d %X'
    time_current = time.strftime(time_fomate)
    with open('a.txt', 'a+') as f:
        f.write('%s End action\n' % time_current)

def test1():
    print('in the test1')

    logs()

def test2():
    print('in the test2')

    logs()

def test3():
    print('in the test3')

    logs()


test1()
test2()
test3()