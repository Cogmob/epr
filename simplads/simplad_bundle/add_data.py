def add_data(*args):
    keys = [i for i in args][::2]
    vals = [i for i in args][1::2]
    def func(i):
        for a, key in keys.items():
            i[key] = vals[a]
        return i
    return func
