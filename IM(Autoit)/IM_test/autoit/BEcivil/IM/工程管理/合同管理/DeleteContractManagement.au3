#Region ;**** 参数创建于 ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** 参数创建于 ACNWrapper_GUI ****
#include-once 

Local $Level, $MenuName
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")

Func ScreenShot( $Level, $Menuname)
   ;Level只能为1,2,3
   ;三级菜单-合同管理
      Select
	  Case $Level = 3 And $Menuname = "删除合同"
		 MouseClick( "", 690, 180)
	  Case $Level = 3 And $Menuname = "确认删除合同"
		 MouseClick( "", 885, 580)
   EndSelect
EndFunc

;删除合同
Func DeleteContractManagement()
	;WinWaitActive($IMtitle, "", 60)
	ScreenShot(3, "删除合同")
	ScreenShot(3, "确认删除合同")
EndFunc

Sleep(5000)
DeleteContractManagement()
