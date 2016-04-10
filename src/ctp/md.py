# encoding: gb2312

from src.util import *
from src.lib import vnctpmd


class NiceMdApi(vnctpmd.MdApi):

    def __init__(self):
        """Constructor"""
        super(NiceMdApi, self).__init__()

    @logger
    def onFrontConnected(self):
        """����������"""
        pass

    @logger
    def onFrontDisconnected(self, n):
        """�������Ͽ�"""
        print n

    @logger
    def onHeartBeatWarning(self, n):
        """��������"""
        print n

    @logger
    def onRspError(self, error, n, last):
        """����"""
        nice_print(error)

    @logger
    def onRspUserLogin(self, data, error, n, last):
        """��½�ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspUserLogout(self, data, error, n, last):
        """�ǳ��ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspSubMarketData(self, data, error, n, last):
        """���ĺ�Լ�ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspUnSubMarketData(self, data, error, n, last):
        """�˶���Լ�ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRtnDepthMarketData(self, data):
        """��������"""
        nice_print(data)

    @logger
    def onRspSubForQuoteRsp(self, data, error, n, last):
        """���ĺ�Լ�ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspUnSubForQuoteRsp(self, data, error, n, last):
        """�˶���Լ�ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRtnForQuoteRsp(self, data):
        """��������"""
        nice_print(data)
