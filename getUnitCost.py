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
    print("휴폐업조회 단가 확인")
    unitCost = closedownService.getUnitCost(testValue.testCorpNum)
    print("조회 단가: %f" % unitCost)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))