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
사업자등록상태조회 (휴폐업조회) 단가를 확인합니다.
- https://developers.popbill.com/reference/closedown/python/api/point#GetUnitCost
"""

try:
    print("=" * 15 + " 사업자등록상태조회 (휴폐업조회) 단가 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    unitCost = closedownService.getUnitCost(CorpNum)

    print("조회 단가 : %f" % unitCost)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
