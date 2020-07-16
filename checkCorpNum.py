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

'''
1건의 사업자에 대한 휴폐업여부를 조회합니다.
'''

try:
    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회할 사업자번호
    targetCorpNum = "1234567890"

    corpState = closedownService.checkCorpNum(CorpNum, targetCorpNum)

    print("=" * 15 + " 휴폐업조회 - 단건 " + "=" * 15)
    print("type(사업자 과세유형) [None-미확인, 1-일반과세자, 2-면세과세자, 3-간이과세자, 4-비영리법인, 국가기관]")
    print("state(휴폐업상태) [None-미확인, 0-등록되지 않은 사업자번호, 1-사업중, 2-폐업, 3-휴업]\n")
    print("corpNum (조회 사업자번호) : %s " % corpState.corpNum)
    print("type (사업자 과세유형) : %s " % corpState.type)
    print("typeDate (과세유형 전환일자) : %s " % corpState.typeDate)
    print("state (휴폐업상태) : %s " % corpState.state)
    print("stateDate (휴폐업 일자) : %s " % corpState.stateDate)
    print("checkDate (국세청 최종 확인일자) : %s " % corpState.checkDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
