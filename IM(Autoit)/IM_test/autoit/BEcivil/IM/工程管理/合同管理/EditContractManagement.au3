#Region ;**** ���������� ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** ���������� ACNWrapper_GUI ****
#include-once 

Global $m1 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "ʩ��������",  "NotFound")
$m2 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "�ܼ�����ʦ",  "NotFound")
$m3 = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\���̹���\��ͬ����\ContractManagementConfig.ini", "Messages", "��Ŀ�ܹ�",  "NotFound")
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIMCofig.ini", "parameters", "IMtitle",  "NotFound")

Local $Level, $MenuName
Local $A1 = 35, $A2 = 90, $A3 = 180, $A4 = 770, $A5 = 1245

Func ScreenShot( $Level, $Menuname)
   ;Levelֻ��Ϊ1,2,3

   ;�����˵�-��ͬ����
      Select

	  Case $Level = 3 And $Menuname = "�༭��ͬ"
		 MouseClick( "", 580, $A3)

   EndSelect


   ;���ܲ˵�-����ʩ����ͬ
      Select

	  Case $Level = 4 And $Menuname = "ʩ��������"
		 MouseClick( "", $A4, 600)
	  Case $Level = 4 And $Menuname = "�ܼ�����ʦ"
		 MouseClick( "", $A5, 550)
	  Case $Level = 4 And $Menuname = "��Ŀ�ܹ�"
		 MouseClick( "", $A5, 600)
	  Case $Level = 4 And $Menuname = "����"
		 MouseClick( "", 890, 835)
   EndSelect
EndFunc

;�༭��ͬ

Func EditContractManagement()
	;WinWaitActive($IMtitle, "", 60)
	ScreenShot(3, "�༭��ͬ")
	ScreenShot(4, "ʩ��������")
	Send($m1)
	ScreenShot(4, "�ܼ�����ʦ")
	Send($m2)
	ScreenShot(4, "��Ŀ�ܹ�")
	Send($m3)
	ScreenShot(4, "����")
EndFunc

Sleep(5000)
EditContractManagement()