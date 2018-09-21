#Region ;**** 参数创建于 ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** 参数创建于 ACNWrapper_GUI ****
#include-once 
Opt("MouseClickDelay", 50) ;鼠标延迟50毫秒点击
Opt("SendKeyDelay", 10) ;输入文本延迟10毫秒

Global $m1 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "合同编号",  "NotFound")
$m2 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "合同金额",  "NotFound")
$m3 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "建设单位",  "NotFound")
$m4 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "施工单位",  "NotFound")
$m5 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "起止桩号",  "NotFound")
$m6 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "合同段长度",  "NotFound")
$m7 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "标段号",  "NotFound")
$m8 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "项目名称",  "NotFound")
$m9 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "监理单位",  "NotFound")
$m10 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "结束桩号",  "NotFound")
$m11 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\ContractManagementConfig.ini", "Messages", "工期",  "NotFound")
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")

Local $Level, $MenuName
Local $A1 = 35, $A2 = 90, $A3 = 180, $A4 = 770, $A5 = 1245


Func ScreenShot( $Level, $Menuname)
   ;Level只能为1,2,3
   ;左侧树菜单
   Select

	  Case $Level = 0 And $Menuname = "选择项目部"
		 MouseClick( "", 50, 170 )
   EndSelect

   ;一级菜单
   Select

	  Case $Level = 1 And $Menuname = "工程管理"
		 MouseClick( "", 470, 40 )
   EndSelect


   ;二级菜单-工程管理
   Select
	  Case $Level = 2 And $Menuname = "合同管理"
		 MouseClick( "", 445, $A2)

   EndSelect

   ;三级菜单-合同管理
      Select
	  Case $Level = 3 And $Menuname = "新增施工合同"
		 MouseClick( "", 470, $A3)

   EndSelect


   ;功能菜单-新增施工合同
      Select
	  Case $Level = 4 And $Menuname = "合同编号"
		 MouseClick( "", $A4, 345)
	  Case $Level = 4 And $Menuname = "合同金额"
		 MouseClick( "", $A4, 395)
	  Case $Level = 4 And $Menuname = "合同签订日期"
		 MouseClick( "", $A4, 450)
	  Case $Level = 4 And $Menuname = "今天签订"
		 MouseClick( "", $A4, 638)
	  Case $Level = 4 And $Menuname = "建设单位"
		 MouseClick( "", $A4, 500)
	  Case $Level = 4 And $Menuname = "施工单位"
		 MouseClick( "", $A4, 550)
	  Case $Level = 4 And $Menuname = "起止桩号"
		 MouseClick( "", $A4, 650)
	  Case $Level = 4 And $Menuname = "合同段长度"
		 MouseClick( "", $A4, 700)
	  Case $Level = 4 And $Menuname = "工期"
		 MouseClick( "", $A4, 745)
	  Case $Level = 4 And $Menuname = "计划开工日期"
		 MouseClick( "", $A4, 755)
	  Case $Level = 4 And $Menuname = "今天开工"
		 MouseClick( "", $A4, 945)
	  Case $Level = 4 And $Menuname = "施工负责人"
		 MouseClick( "", $A4, 600)
	  Case $Level = 4 And $Menuname = "标段号"
		 MouseClick( "", $A5, 345)
	  Case $Level = 4 And $Menuname = "项目名称"
		 MouseClick( "", $A5, 395)
	  Case $Level = 4 And $Menuname = "监理单位"
		 MouseClick( "", $A5, 500)
	  Case $Level = 4 And $Menuname = "总监理工程师"
		 MouseClick( "", $A5, 550)
	  Case $Level = 4 And $Menuname = "项目总工"
		 MouseClick( "", $A5, 600)
	  Case $Level = 4 And $Menuname = "结束桩号"
		 MouseClick( "", $A5, 650)
	  Case $Level = 4 And $Menuname = "计划完工日期"
		 MouseClick( "", $A5, 755)
	  Case $Level = 4 And $Menuname = "今天完工"
		 MouseClick( "", $A5, 945)
	  Case $Level = 4 And $Menuname = "保存"
		 MouseClick( "", 890, 835)

   EndSelect



EndFunc   ;==>MyMouseClick

Func CreatContractManagement()
	;Sleep(3000)
	;WinWaitActive($IMtitle, "", 60)
	ScreenShot(0, "选择项目部")
	ScreenShot(1, "工程管理")
	ScreenShot(2, "合同管理")
	ScreenShot(3, "新增施工合同")
	ScreenShot(4, "合同编号")
	Send($m1)
	ScreenShot(4, "合同金额")
	Send($m2)
	ScreenShot(4, "合同签订日期")
	ScreenShot(4, "今天签订")
	ScreenShot(4, "建设单位")
	Send($m3)
	ScreenShot(4, "施工单位")
	Send($m4)
	ScreenShot(4, "起止桩号")
	Send($m5)
	ScreenShot(4, "合同段长度")
	Send($m6)
	ScreenShot(4, "计划开工日期")
	ScreenShot(4, "今天开工")
	ScreenShot(4, "标段号")
	Send($m7)
	ScreenShot(4, "项目名称")
	Send($m8)
	ScreenShot(4, "监理单位")
	Send($m9)
	ScreenShot(4, "结束桩号")
	Send($m10)
	ScreenShot(4, "计划完工日期")
	ScreenShot(4, "今天完工")
	MouseMove(960, 590)
	MouseWheel("down", 2)
	ScreenShot(4, "工期")
	Send($m11)
	ScreenShot(4, "保存")
EndFunc

Sleep(5000)
CreatContractManagement()