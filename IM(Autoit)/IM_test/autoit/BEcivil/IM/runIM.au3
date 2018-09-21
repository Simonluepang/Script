#Region ;**** 参数创建于 ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** 参数创建于 ACNWrapper_GUI ****
#include-once 


Opt("MouseClickDelay", 50) ;鼠标延迟50毫秒点击
Opt("SendKeyDelay", 10) ;输入文本延迟10毫秒


Global $IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")
$process_ZYDL = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "process_ZYDL",  "NotFound")
$process_ZYCA = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "process_ZYCA",  "NotFound")




Func ScreenShot( $Level, $Menuname)
   ;Level只能为1,2,3
   ;市政内部菜单
   Select
	  Case $Level = 0 And $Menuname = "资料"
		 MouseClick( "", 360, 40 )
	  Case $Level = 0 And $Menuname = "质检计量"
		 MouseClick( "", 190, 85 )
   EndSelect
EndFunc


;启动IM
Sleep(3000)
ScreenShot(0, "资料")
ScreenShot(0, "质检计量")
WinWaitActive($IMtitle, "", 60)
WinActivate($IMtitle)
WinSetState($IMtitle, "", @SW_MAXIMIZE)
WinWaitActive("重要提示", "", 10)
If ProcessExists($process_ZYCA) Then ProcessClose($process_ZYCA)
WinWaitActive("确认", "", 10)
If ProcessExists($process_ZYDL) Then ProcessClose($process_ZYDL)