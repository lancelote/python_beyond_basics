class CallCount(object):

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello %s' % name)

hello('Pavel')
hello('Yuri')
print(hello.count)
