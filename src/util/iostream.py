# encoding: gb2312


def nice_print(d):
    """���ռ�ֵ��ӡһ���ֵ�"""
    print "����Ϊ��" + str(type(d))
    if isinstance(d, dict):
        for key, value in d.items():
            print key + ': ' + str(value)
    else:
        print d


def logger(func):
    """��װ�����������������"""
    def wrapper(*args, **kw):
        print ""
        print str(func.__name__)
        return func(*args, **kw)
    return wrapper

