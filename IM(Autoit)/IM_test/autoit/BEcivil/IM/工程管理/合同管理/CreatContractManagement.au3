#Region ;**** ���������� ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** ���������� ACNWrapper_GUI ****
#include-once 
Opt("MouseClickDelay", 50) ;����ӳ�50������
Opt("SendKeyDelay", 10) ;�����ı��ӳ�10����

Global $m1 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "��ͬ���",  "NotFound")
$m2 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "��ͬ���",  "NotFound")
$m3 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "���赥λ",  "NotFound")
$m4 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "ʩ����λ",  "NotFound")
$m5 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "��ֹ׮��",  "NotFound")
$m6 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "��ͬ�γ���",  "NotFound")
$m7 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "��κ�",  "NotFound")
$m8 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "��Ŀ����",  "NotFound")
$m9 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "����λ",  "NotFound")
$m10 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "����׮��",  "NotFound")
$m11 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "����",  "NotFound")
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")

Local $Level, $MenuName
Local $A1 = 35, $A2 = 90, $A3 = 180, $A4 = 770, $A5 = 1245


Func ScreenShot( $Level, $Menuname)
   ;Levelֻ��Ϊ1,2,3
   ;������˵�
   Select

	  Case $Level = 0 And $Menuname = "ѡ����Ŀ��"
		 MouseClick( "", 50, 170 )
   EndSelect

   ;һ���˵�
   Select

	  Case $Level = 1 And $Menuname = "���̹���"
		 MouseClick( "", 470, 40 )
   EndSelect


   ;�����˵�-���̹���
   Select
	  Case $Level = 2 And $Menuname = "��ͬ����"
		 MouseClick( "", 445, $A2)

   EndSelect

   ;�����˵�-��ͬ����
      Select
	  Case $Level = 3 And $Menuname = "����ʩ����ͬ"
		 MouseClick( "", 470, $A3)

   EndSelect


   ;���ܲ˵�-����ʩ����ͬ
      Select
	  Case $Level = 4 And $Menuname = "��ͬ���"
		 MouseClick( "", $A4, 345)
	  Case $Level = 4 And $Menuname = "��ͬ���"
		 MouseClick( "", $A4, 395)
	  Case $Level = 4 And $Menuname = "��ͬǩ������"
		 MouseClick( "", $A4, 450)
	  Case $Level = 4 And $Menuname = "����ǩ��"
		 MouseClick( "", $A4, 638)
	  Case $Level = 4 And $Menuname = "���赥λ"
		 MouseClick( "", $A4, 500)
	  Case $Level = 4 And $Menuname = "ʩ����λ"
		 MouseClick( "", $A4, 550)
	  Case $Level = 4 And $Menuname = "��ֹ׮��"
		 MouseClick( "", $A4, 650)
	  Case $Level = 4 And $Menuname = "��ͬ�γ���"
		 MouseClick( "", $A4, 700)
	  Case $Level = 4 And $Menuname = "����"
		 MouseClick( "", $A4, 745)
	  Case $Level = 4 And $Menuname = "�ƻ���������"
		 MouseClick( "", $A4, 755)
	  Case $Level = 4 And $Menuname = "���쿪��"
		 MouseClick( "", $A4, 945)
	  Case $Level = 4 And $Menuname = "ʩ��������"
		 MouseClick( "", $A4, 600)
	  Case $Level = 4 And $Menuname = "��κ�"
		 MouseClick( "", $A5, 345)
	  Case $Level = 4 And $Menuname = "��Ŀ����"
		 MouseClick( "", $A5, 395)
	  Case $Level = 4 And $Menuname = "����λ"
		 MouseClick( "", $A5, 500)
	  Case $Level = 4 And $Menuname = "�ܼ�����ʦ"
		 MouseClick( "", $A5, 550)
	  Case $Level = 4 And $Menuname = "��Ŀ�ܹ�"
		 MouseClick( "", $A5, 600)
	  Case $Level = 4 And $Menuname = "����׮��"
		 MouseClick( "", $A5, 650)
	  Case $Level = 4 And $Menuname = "�ƻ��깤����"
		 MouseClick( "", $A5, 755)
	  Case $Level = 4 And $Menuname = "�����깤"
		 MouseClick( "", $A5, 945)
	  Case $Level = 4 And $Menuname = "����"
		 MouseClick( "", 890, 835)

   EndSelect



EndFunc   ;==>MyMouseClick

Func CreatContractManagement()
	;Sleep(3000)
	;WinWaitActive($IMtitle, "", 60)
	ScreenShot(0, "ѡ����Ŀ��")
	ScreenShot(1, "���̹���")
	ScreenShot(2, "��ͬ����")
	ScreenShot(3, "����ʩ����ͬ")
	ScreenShot(4, "��ͬ���")
	Send($m1)
	ScreenShot(4, "��ͬ���")
	Send($m2)
	ScreenShot(4, "��ͬǩ������")
	ScreenShot(4, "����ǩ��")
	ScreenShot(4, "���赥λ")
	Send($m3)
	ScreenShot(4, "ʩ����λ")
	Send($m4)
	ScreenShot(4, "��ֹ׮��")
	Send($m5)
	ScreenShot(4, "��ͬ�γ���")
	Send($m6)
	ScreenShot(4, "�ƻ���������")
	ScreenShot(4, "���쿪��")
	ScreenShot(4, "��κ�")
	Send($m7)
	ScreenShot(4, "��Ŀ����")
	Send($m8)
	ScreenShot(4, "����λ")
	Send($m9)
	ScreenShot(4, "����׮��")
	Send($m10)
	ScreenShot(4, "�ƻ��깤����")
	ScreenShot(4, "�����깤")
	MouseMove(960, 590)
	MouseWheel("down", 2)
	ScreenShot(4, "����")
	Send($m11)
	ScreenShot(4, "����")
EndFunc

Sleep(5000)
CreatContractManagement()