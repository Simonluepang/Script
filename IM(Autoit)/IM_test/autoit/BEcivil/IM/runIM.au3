#Region ;**** ���������� ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** ���������� ACNWrapper_GUI ****
#include-once 


Opt("MouseClickDelay", 50) ;����ӳ�50������
Opt("SendKeyDelay", 10) ;�����ı��ӳ�10����


Global $IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")
$process_ZYDL = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "process_ZYDL",  "NotFound")
$process_ZYCA = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "process_ZYCA",  "NotFound")




Func ScreenShot( $Level, $Menuname)
   ;Levelֻ��Ϊ1,2,3
   ;�����ڲ��˵�
   Select
	  Case $Level = 0 And $Menuname = "����"
		 MouseClick( "", 360, 40 )
	  Case $Level = 0 And $Menuname = "�ʼ����"
		 MouseClick( "", 190, 85 )
   EndSelect
EndFunc


;����IM
Sleep(3000)
ScreenShot(0, "����")
ScreenShot(0, "�ʼ����")
WinWaitActive($IMtitle, "", 60)
WinActivate($IMtitle)
WinSetState($IMtitle, "", @SW_MAXIMIZE)
WinWaitActive("��Ҫ��ʾ", "", 10)
If ProcessExists($process_ZYCA) Then ProcessClose($process_ZYCA)
WinWaitActive("ȷ��", "", 10)
If ProcessExists($process_ZYDL) Then ProcessClose($process_ZYDL)