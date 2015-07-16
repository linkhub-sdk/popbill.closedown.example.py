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
    print("팝빌 URL 확인")
    # LOGIN : 팝빌 로그인 URL, CHRG : 포인트충전 URL
    url = closedownService.getPopbillURL(testValue.testCorpNum,testValue.testUserID,"LOGIN")  
    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))