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

from popbill import ContactInfo, ClosedownService, PopbillException

closedownService = ClosedownService(testValue.LinkID, testValue.SecretKey)
closedownService.IsTest = testValue.IsTest
closedownService.IPRestrictOnOff = testValue.IPRestrictOnOff
closedownService.UseStaticIP = testValue.UseStaticIP

'''
팝빌 연동회원 사업자의 담당자 정보를 수정합니다.
- https://docs.popbill.com/closedown/python/api#UpdateContact
'''

try:
    print("=" * 15 + " 담당자 정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    updateInfo = ContactInfo(

        # 담당자 아이디
        id=UserID,

        # 담당자 성명 (최대 100자)
        personName="담당자_성명",

        # 담당자 연락처 (최대 20자)
        tel="010-111-111",

        # 담당자 휴대폰번호 (최대 20자)
        hp="010-111-111",

        # 담당자 팩스번호 (최대 20자)
        fax="070-111-222",

        # 담당자 메일주소 (최대 100자)
        email="test@test.com",

        # 회사조회 권한여부, True(회사조회) False(개인조회)
        searchAllAllowYN=True,

        # 관리자 권한여부, True(관리자), False(사용자)
        mgrYN=True
    )

    result = closedownService.updateContact(CorpNum, updateInfo, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
