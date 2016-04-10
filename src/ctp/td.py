# encoding: gb2312

from src.util import *
from src.lib import vnctptd


class NiceTdApi(vnctptd.TdApi):

    def __init__(self):
        """Constructor"""
        super(NiceTdApi, self).__init__()
        self.brokerID = ''
        self.userID = ''
        self.frontID = ''
        self.sessionID = ''

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
        self.brokerID = data['BrokerID']
        self.userID = data['UserID']
        self.frontID = data['FrontID']
        self.sessionID = data['SessionID']

    @logger
    def onRspUserLogout(self, data, error, n, last):
        """登出回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspQrySettlementInfo(self, data, error, n, last):
        """查询结算信息回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspSettlementInfoConfirm(self, data, error, n, last):
        """确认结算信息回报"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspQryInstrument(self, data, error, n, last):
        """查询合约回报"""
        nice_print(data)
        nice_print(error)
        print n
        print last

