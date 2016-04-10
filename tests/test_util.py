# encoding: gb2312

import nose
from src.util import *


def test_nice_print():
    """测试nice_print函数"""
    try:
        # 测试数字
        number_var = 1234
        nice_print(number_var)
        # 测试字符串
        nice_print('This is a string sequence')
        # 测试数组
        nice_print(['1', '2', '3'])
        # 测试对象
        nice_print(dict(a=1, b=2))
        assert True
    except Exception:
        assert False
        raise Exception


if __name__ == '__main__':
    nose.runmodule()


