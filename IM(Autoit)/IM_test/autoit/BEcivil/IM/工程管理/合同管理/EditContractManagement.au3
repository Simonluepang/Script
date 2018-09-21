#Region ;**** 参数创建于 ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** 参数创建于 ACNWrapper_GUI ****
#include-once 

Global $m1 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "施工负责人",  "NotFound")
$m2 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "总监理工程师",  "NotFound")
$m3 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "项目总工",  "NotFound")
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")

Local $Level, $MenuName
Local $A1 = 35, $A2 = 90, $A3 = 180, $A4 = 770, $A5 = 1245

Func ScreenShot( $Level, $Menuname)
   ;Level只能为1,2,3

   ;三级菜单-合同管理
      Select

	  Case $Level = 3 And $Menuname = "编辑合同"
		 MouseClick( "", 580, $A3)

   EndSelect


   ;功能菜单-新增施工合同
      Select

	  Case $Level = 4 And $Menuname = "施工负责人"
		 MouseClick( "", $A4, 600)
	  Case $Level = 4 And $Menuname = "总监理工程师"
		 MouseClick( "", $A5, 550)
	  Case $Level = 4 And $Menuname = "项目总工"
		 MouseClick( "", $A5, 600)
	  Case $Level = 4 And $Menuname = "保存"
		 MouseClick( "", 890, 835)
   EndSelect
EndFunc

;编辑合同

Func EditContractManagement()
	;WinWaitActive($IMtitle, "", 60)
	ScreenShot(3, "编辑合同")
	ScreenShot(4, "施工负责人")
	Send($m1)
	ScreenShot(4, "总监理工程师")
	Send($m2)
	ScreenShot(4, "项目总工")
	Send($m3)
	ScreenShot(4, "保存")
EndFunc

Sleep(5000)
EditContractManagement()