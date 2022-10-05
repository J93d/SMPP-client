def error_codes(code):
    if hex(code) == hex(0x00000000):
        return str("ESME_ROK")
    elif hex(code) == hex(0x00000001):
        return str("ESME_RINVMSGLEN")
    elif hex(code) == hex(0x00000002):
        return str("ESME_RINVCMDLEN")
    elif hex(code) == hex(0x00000003):
        return str("ESME_RINVCMDID")
    elif hex(code) == hex(0x00000004):
        return str("ESME_RINVBNDSTS")
    elif hex(code) == hex(0x00000005):
        return str("ESME_RALYBND")
    elif hex(code) == hex(0x00000006):
        return str("ESME_RINVPRTFLG")
    elif hex(code) == hex(0x00000007):
        return str("ESME_RINVREGDLVFLG")
    elif hex(code) == hex(0x00000008):
        return str("ESME_RSYSERR")
    elif hex(code) == hex(0x0000000A):
        return str("ESME_RINVSRCADR")
    elif hex(code) == hex(0x0000000B):
        return str("ESME_RINVDSTADR")
    elif hex(code) == hex(0x0000000C):
        return str("ESME_RINVMSGID")
    elif hex(code) == hex(0x0000000D):
        return str("ESME_RBINDFAIL")
    elif hex(code) == hex(0x0000000E):
        return str("ESME_RINVPASWD")
    elif hex(code) == hex(0x0000000F):
        return str("ESME_RINVSYSID")
    elif hex(code) == hex(0x00000011):
        return str("ESME_RCANCELFAIL")
    elif hex(code) == hex(0x00000013):
        return str("ESME_RREPLACEFAIL")
    elif hex(code) == hex(0x00000014):
        return str("ESME_RMSGQFUL")
    elif hex(code) == hex(0x00000015):
        return str("ESME_RINVSERTYP")
    elif hex(code) == hex(0x00000033):
        return str("ESME_RINVNUMDESTS")
    elif hex(code) == hex(0x00000034):
        return str("ESME_RINVDLNAME")
    elif hex(code) == hex(0x00000040):
        return str("ESME_RINVDESTFLAG")
    elif hex(code) == hex(0x00000042):
        return str("ESME_RINVSUBREP")
    elif hex(code) == hex(0x00000043):
        return str("ESME_RINVESMCLASS")
    elif hex(code) == hex(0x00000044):
        return str("ESME_RCNTSUBDL")
    elif hex(code) == hex(0x00000045):
        return str("ESME_RSUBMITFAIL")
    elif hex(code) == hex(0x00000048):
        return str("ESME_RINVSRCTON")
    elif hex(code) == hex(0x00000049):
        return str("ESME_RINVSRCNPI")
    elif hex(code) == hex(0x00000050):
        return str("ESME_RINVDSTTON")
    elif hex(code) == hex(0x00000051):
        return str("ESME_RINVDSTNPI")
    elif hex(code) == hex(0x00000053):
        return str("ESME_RINVSYSTYP")
    elif hex(code) == hex(0x00000054):
        return str("ESME_RINVREPFLAG")
    elif hex(code) == hex(0x00000055):
        return str("ESME_RINVNUMMSGS")
    elif hex(code) == hex(0x00000058):
        return str("ESME_RTHROTTLED")
    elif hex(code) == hex(0x00000061):
        return str("ESME_RINVSCHED")
    elif hex(code) == hex(0x00000062):
        return str("ESME_RINVEXPIRY")
    elif hex(code) == hex(0x00000063):
        return str("ESME_RINVDFTMSGID")
    elif hex(code) == hex(0x00000064):
        return str("ESME_RX_T_APPN")
    elif hex(code) == hex(0x00000065):
        return str("ESME_RX_P_APPN")
    elif hex(code) == hex(0x00000066):
        return str("ESME_RX_R_APPN")
    elif hex(code) == hex(0x00000067):
        return str("ESME_RQUERYFAIL")
    elif hex(code) == hex(0x000000C0):
        return str("ESME_RINVTLVSTREAM")
    elif hex(code) == hex(0x000000C1):
        return str("ESME_RTLVNOTALLWD")
    elif hex(code) == hex(0x000000C2):
        return str("ESME_RINVTLVLEN")
    elif hex(code) == hex(0x000000C3):
        return str("ESME_RMISSINGTLV")
    elif hex(code) == hex(0x000000C4):
        return str("ESME_RINVTLVVAL")
    elif hex(code) == hex(0x000000FE):
        return str("ESME_RDELIVERYFAILURE")
    elif hex(code) == hex(0x000000FF):
        return str("ESME_RUNKNOWNERR")
    elif hex(code) == hex(0x00000100):
        return str("ESME_RSERTYPUNAUTH")
    elif hex(code) == hex(0x00000101):
        return str("ESME_RPROHIBITED")
    elif hex(code) == hex(0x00000102):
        return str("ESME_RSERTYPUNAVAIL")
    elif hex(code) == hex(0x00000103):
        return str("ESME_RSERTYPDENIED")
    elif hex(code) == hex(0x00000104):
        return str("ESME_RINVDCS")
    elif hex(code) == hex(0x00000105):
        return str("ESME_RINVSRCADDRSUBUNIT")
    elif hex(code) == hex(0x00000106):
        return str("ESME_RINVDSTADDRSUBUNIT")
    elif hex(code) == hex(0x00000107):
        return str("ESME_RINVBCASTFREQINT")
    elif hex(code) == hex(0x00000108):
        return str("ESME_RINVBCASTALIAS_NAME")
    elif hex(code) == hex(0x00000109):
        return str("ESME_RINVBCASTAREAFMT")
    elif hex(code) == hex(0x0000010A):
        return str("ESME_RINVNUMBCAST_AREAS")
    elif hex(code) == hex(0x0000010B):
        return str("ESME_RINVBCASTCNTTYPE")
    elif hex(code) == hex(0x0000010C):
        return str("ESME_RINVBCASTMSGCLASS")
    elif hex(code) == hex(0x0000010D):
        return str("ESME_RBCASTFAIL")
    elif hex(code) == hex(0x0000010E):
        return str("ESME_RBCASTQUERYFAIL")
    elif hex(code) == hex(0x0000010F):
        return str("ESME_RBCASTCANCELFAIL")
    elif hex(code) == hex(0x00000110):
        return str("ESME_RINVBCAST_REP")
    elif hex(code) == hex(0x00000111):
        return str("ESME_RINVBCASTSRVGRP")
    elif hex(code) == hex(0x00000112):
        return str("ESME_RINVBCASTCHANIND")
    elif hex(code) >= hex(0x00000400) and hex(code) <= hex(0x000004FF):
        return str("MC vendor specific errors")
    else:
        return str("Reserved")