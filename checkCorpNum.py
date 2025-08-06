# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import ClosedownService, PopbillException

closedownService = ClosedownService(testValue.LinkID, testValue.SecretKey)
closedownService.IsTest = testValue.IsTest
closedownService.IPRestrictOnOff = testValue.IPRestrictOnOff
closedownService.UseStaticIP = testValue.UseStaticIP
closedownService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
사업자번호 1건에 대한 사업자등록상태(휴폐업)를 확인합니다.
- https://developers.popbill.com/reference/closedown/python/api/check#CheckCorpNum
"""

try:
    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회할 사업자번호
    targetCorpNum = "6798700433"

    corpState = closedownService.checkCorpNum(CorpNum, targetCorpNum)

    print("=" * 15 + " 사업자등록상태조회 (휴폐업조회) - 단건 " + "=" * 15)


    print("corpNum (조회 사업자번호) : %s " % corpState.corpNum)
    print("taxType (사업자 과세유형) : %s " % corpState.taxType)
    print("typeDate (과세유형 전환일자) : %s " % corpState.typeDate)
    print("state (휴폐업상태) : %s " % corpState.state)
    print("stateDate (휴폐업일자) : %s " % corpState.stateDate)
    print("checkDate (국세청 확인일자) : %s " % corpState.checkDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
