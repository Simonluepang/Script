#include-once 
#include <ScreenCapture.au3>


Opt("PixelCoordMode", 0)        ;1=绝对位置, 0=相对位置, 2=客户区
Opt("WinTitleMatchMode", 2)     ;1=开头, 2=子串, 3=完全, 4=高级 , -1 to -4=Nocase
Opt("WinTextMatchMode", 2)      ;1=完全匹配, 2=快速匹配

Global $title = "Luban Explorer"
$IMtitle = "Luban Inspector（Civil）"
; ==========================================================================================================
; 公共函数
; 点击主界面位置: MyMouseClick($window, $text, $x, $y, $button = "Main", $clicks = "1" )
; 移动鼠标位置: MyMouseMove($window, $text, $x, $y)
; 拖拽鼠标位置: MyMouseClickDrag($window, $text, $x1, $y1, $x2, $y2)
; 截屏指定窗口: MyScreenCapture($PicName, $window, $text)
; 启动软件: start($path, $username, $password, $ip, $epNum)
; 打开工程: OpenProject($projTree)	如果被选工程选择后没有排在第一行，则此函数无效
; ==========================================================================================================

; 点击主界面位置
Func MyMouseClick($window, $text, $x, $y, $button = "Main", $clicks = "1" )
	$pos = WinGetPos($window, $text) 
	MouseClick($button, $x + $pos[0], $y + $pos[1], $clicks)
EndFunc

; 移动鼠标位置
Func MyMouseMove($window, $text, $x, $y)
	$pos = WinGetPos($window, $text) 
	MouseMove($x + $pos[0], $y + $pos[1])
EndFunc

; 拖拽鼠标位置
Func MyMouseClickDrag($window, $text, $x1, $y1, $x2, $y2)
	$pos = WinGetPos($window, $text) 
	MouseClickDrag("Main", $x1 + $pos[0], $y1 + $pos[1], $x2 + $pos[0], $y2 + $pos[1])
EndFunc

; 截屏指定窗口: 
Func MyScreenCapture($PicName, $window, $text)
	$pos = WinGetPos($window, $text) 
	_ScreenCapture_Capture($PicName, $pos[0], $pos[1], $pos[0] + $pos[2], $pos[1] + $pos[3])
EndFunc

; 启动软件
Func start($path, $username, $password, $ip, $epNum)
	ShellExecute($path)														;启动壳
	WinWait("用户登录")														;等待登录窗口
	WinActivate("用户登录")
	ControlSetText("用户登录", "", "[CLASS:Edit; INSTANCE:1]", $username)	;设置用户名
	ControlSetText("用户登录", "", "[CLASS:Edit; INSTANCE:2]", $password)	;设置密码
	ControlSetText("用户登录", "", "[CLASS:Edit; INSTANCE:3]", $ip)			;设置服务器地址
	ControlFocus("用户登录","","[CLASS:Button; INSTANCE:1]")				;鼠标移动至登录按钮
	ControlClick("用户登录","","[CLASS:Button; INSTANCE:1]")				;点击登录
	Sleep(1000)
	WinWaitActive("", "lbComboBox", 10)										;等待选择企业窗口,10秒超时
	If WinExists("", "lbComboBox") Then												;若账号只有一个企业则不会弹出此框
		ControlFocus("","lbComboBox","[CLASS:AfxWnd110u; INSTANCE:1]")		;鼠标移动至选择框
		ControlClick("","lbComboBox","[CLASS:AfxWnd110u; INSTANCE:1]")		;点击选择企业框
		MyMouseClick("", "lbComboBox", 98, 138  + 26 * ($epNum - 1))		;选择第$epNum个企业
		ControlFocus("","","[CLASS:Button; INSTANCE:1]")					;鼠标移动至确定
		ControlClick("","","[CLASS:Button; INSTANCE:1]")					;点击确定
	EndIf
EndFunc

; 打开工程
Func OpenProject($projTree)
	MyMouseClick($title, "", 113, 87)										;点击打开工程
	WinWaitActive("选择工程")
	If ControlTreeView ( "选择工程", "", "[CLASS:SysTreeView32; INSTANCE:1]", "Exists", $projTree) = 1 Then		;判断节点是否存在
		ControlTreeView ( "选择工程", "", "[CLASS:SysTreeView32; INSTANCE:1]", "Select", $projTree )			;若节点存在则选择节点
		MyMouseClick("选择工程", "", 170, 70, "Main", "2")								;双击第一个工程，不一定是被选中项
		WinWait("处理状态", "隐藏", 10)
		If WinExists("处理状态", "隐藏") Then WinWaitClose("处理状态", "隐藏")
	Else
		MsgBox(0,"提示", $projTree &"节点不存在！")						;若节点不存在则提示
	EndIf
EndFunc

