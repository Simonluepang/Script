#Region ;**** ���������� ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** ���������� ACNWrapper_GUI ****
#include-once 

Local $Level, $MenuName
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")

Func ScreenShot( $Level, $Menuname)
   ;Levelֻ��Ϊ1,2,3
   ;�����˵�-��ͬ����
      Select
	  Case $Level = 3 And $Menuname = "ɾ����ͬ"
		 MouseClick( "", 690, 180)
	  Case $Level = 3 And $Menuname = "ȷ��ɾ����ͬ"
		 MouseClick( "", 885, 580)
   EndSelect
EndFunc

;ɾ����ͬ
Func DeleteContractManagement()
	;WinWaitActive($IMtitle, "", 60)
	ScreenShot(3, "ɾ����ͬ")
	ScreenShot(3, "ȷ��ɾ����ͬ")
EndFunc

Sleep(5000)
DeleteContractManagement()
