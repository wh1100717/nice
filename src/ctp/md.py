# encoding: gb2312

from src.util import *
from src.lib import vnctpmd


class NiceMdApi(vnctpmd.MdApi):

    def __init__(self):
        """Constructor"""
        super(NiceMdApi, self).__init__()

    @logger
    def onFrontConnected(self):
        """服务器连接"""
        pass

    @logger
    def onFrontDisconnected(self, n):
        """服务器断开"""
        print n

    @logger
    def onHeartBeatWarning(self, n):
        """心跳报警"""
        print n

    @logger
    def onRspError(self, error, n, last):
        """错误"""
        nice_print(error)

    @logger
    def onRspUserLogin(self, data, error, n, last):
        """登陆回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspUserLogout(self, data, error, n, last):
        """登出回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspSubMarketData(self, data, error, n, last):
        """订阅合约回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspUnSubMarketData(self, data, error, n, last):
        """退订合约回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRtnDepthMarketData(self, data):
        """行情推送"""
        nice_print(data)

    @logger
    def onRspSubForQuoteRsp(self, data, error, n, last):
        """订阅合约回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspUnSubForQuoteRsp(self, data, error, n, last):
        """退订合约回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRtnForQuoteRsp(self, data):
        """行情推送"""
        nice_print(data)
