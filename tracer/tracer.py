class Trace(object):

    def __init__(self):
        self.enabled = True

    def __call__(self, func):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling %s' % func)
            return func(*args, **kwargs)
        return wrap

tracer = Trace()


@tracer
def rotate_list(lst):
    return lst[1:] + [lst[0]]

l = rotate_list([1, 2, 3])
l = rotate_list(l)
tracer.enabled = False

l = rotate_list(l)
l = rotate_list(l)
