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

'''
다수의 사업자에 대한 휴폐업여부를 조회합니다. (최대 1000건)
'''

try:
    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회할 사업자번호 배열, 최대 1000건
    targetCorpNumList = []
    targetCorpNumList.append("6798700433")
    targetCorpNumList.append("123-45-67890")

    CorpStateList = closedownService.checkCorpNums(CorpNum, targetCorpNumList)

    print("=" * 15 + " 휴폐업조회 - 대량 " + "=" * 15)
    print("type(사업자 과세유형) [None-미확인, 1-일반과세자, 2-면세과세자, 3-간이과세자, 4-비영리법인, 국가기관]")
    print("state(휴폐업상태) [None-미확인, 0-등록되지 않은 사업자번호, 1-사업중, 2-폐업, 3-휴업]\n")
    for info in CorpStateList:
        print("corpNum (조회 사업자번호) : %s " % info.corpNum)
        print("type (사업자 과세유형) : %s " % info.type)
        print("typeDate (과세유형 전환일자) : %s " % info.typeDate)
        print("state (휴폐업상태) : %s " % info.state)
        print("stateDate (휴폐업일자) : %s " % info.stateDate)
        print("checkDate (국세청 최종 확인일자) : %s " % info.checkDate) + '\n'

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
