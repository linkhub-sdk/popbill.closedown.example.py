# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import ClosedownService, PopbillException

closedownService = ClosedownService(testValue.LinkID, testValue.SecretKey)
closedownService.IsTest = testValue.IsTest
closedownService.IPRestrictOnOff = testValue.IPRestrictOnOff
closedownService.UseStaticIP = testValue.UseStaticIP
closedownService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
파트너의 잔여포인트를 확인합니다.
- https://docs.popbill.com/closedown/python/api#GetPartnerBalance
'''

try:
    print("=" * 15 + " 파트너 잔여포인트 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    balance = closedownService.getPartnerBalance(CorpNum)

    print("파트너 잔여포인트: %f" % balance)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
