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
사업자번호 1건에 대한 휴폐업정보를 확인합니다.
- https://docs.popbill.com/closedown/python/api#CheckCorpNum
'''

try:
    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회할 사업자번호
    targetCorpNum = "6798700433"

    corpState = closedownService.checkCorpNum(CorpNum, targetCorpNum)

    print("=" * 15 + " 휴폐업조회 - 단건 " + "=" * 15)
    print("taxType(사업자 과세유형) [None-미확인, 10-일반과세자, 20-면세과세자, 30-간이과세자, 31-간이과세자(세금계산서 발급사업자), 40-비영리법인, 국가기관]")
    print("state(휴폐업상태) [None-미확인, 0-등록되지 않은 사업자번호, 1-사업중, 2-폐업, 3-휴업]\n")
    
    print("corpNum (조회 사업자번호) : %s " % corpState.corpNum)
    print("taxType (사업자 과세유형) : %s " % corpState.taxType)
    print("typeDate (과세유형 전환일자) : %s " % corpState.typeDate)
    print("state (휴폐업상태) : %s " % corpState.state)
    print("stateDate (휴폐업 일자) : %s " % corpState.stateDate)
    print("checkDate (국세청 최종 확인일자) : %s " % corpState.checkDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
