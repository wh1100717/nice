# encoding: gb2312

import nose
from src.util import *


def test_nice_print():
    """����nice_print����"""
    try:
        # ��������
        number_var = 1234
        nice_print(number_var)
        # �����ַ���
        nice_print('This is a string sequence')
        # ��������
        nice_print(['1', '2', '3'])
        # ���Զ���
        nice_print(dict(a=1, b=2))
        assert True
    except Exception:
        assert False
        raise Exception


if __name__ == '__main__':
    nose.runmodule()


