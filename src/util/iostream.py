# encoding: gb2312


def nice_print(d):
    """按照键值打印一个字典"""
    print "类型为：" + str(type(d))
    if isinstance(d, dict):
        for key, value in d.items():
            print key + ': ' + str(value)
    else:
        print d


def logger(func):
    """简单装饰器用于输出函数名"""
    def wrapper(*args, **kw):
        print ""
        print str(func.__name__)
        return func(*args, **kw)
    return wrapper

