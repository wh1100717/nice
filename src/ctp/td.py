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
        self.brokerID = data['BrokerID']
        self.userID = data['UserID']
        self.frontID = data['FrontID']
        self.sessionID = data['SessionID']

    @logger
    def onRspUserLogout(self, data, error, n, last):
        """�ǳ��ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspQrySettlementInfo(self, data, error, n, last):
        """��ѯ������Ϣ�ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspSettlementInfoConfirm(self, data, error, n, last):
        """ȷ�Ͻ�����Ϣ�ر�"""
        nice_print(data)
        nice_print(error)

    @logger
    def onRspQryInstrument(self, data, error, n, last):
        """��ѯ��Լ�ر�"""
        nice_print(data)
        nice_print(error)
        print n
        print last

