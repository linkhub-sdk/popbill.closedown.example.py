# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import ClosedownService,PopbillException

closedownService =  ClosedownService(testValue.LinkID,testValue.SecretKey)
closedownService.IsTest = testValue.IsTest
  
try:
    print("휴폐업조회 - 단건")
    print("state (휴폐업상태) : None-알수없음, 0-등록되지 않은 사업자번호, 1-사업중, 2-폐업, 3-휴업")
    print("type (사업유형) : None-알수없음, 1-일반과세자, 2-면세과세자, 3-간이과세자, 4-비영리법인, 국가기관\n")

    checkCorpNum = "4108621884"     # 조회할 사업자번호
    corpState = closedownService.checkCorpNum(testValue.testCorpNum,checkCorpNum)


    for key, value in corpState.__dict__.items():
        if not key.startswith("__"):
            print("%s : %s" % (key,value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))