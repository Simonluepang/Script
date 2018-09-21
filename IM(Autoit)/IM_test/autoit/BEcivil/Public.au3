#include-once 
#include <ScreenCapture.au3>


Opt("PixelCoordMode", 0)        ;1=����λ��, 0=���λ��, 2=�ͻ���
Opt("WinTitleMatchMode", 2)     ;1=��ͷ, 2=�Ӵ�, 3=��ȫ, 4=�߼� , -1 to -4=Nocase
Opt("WinTextMatchMode", 2)      ;1=��ȫƥ��, 2=����ƥ��

Global $title = "Luban Explorer"
$IMtitle = "Luban Inspector��Civil��"
; ==========================================================================================================
; ��������
; ���������λ��: MyMouseClick($window, $text, $x, $y, $button = "Main", $clicks = "1" )
; �ƶ����λ��: MyMouseMove($window, $text, $x, $y)
; ��ק���λ��: MyMouseClickDrag($window, $text, $x1, $y1, $x2, $y2)
; ����ָ������: MyScreenCapture($PicName, $window, $text)
; �������: start($path, $username, $password, $ip, $epNum)
; �򿪹���: OpenProject($projTree)	�����ѡ����ѡ���û�����ڵ�һ�У���˺�����Ч
; ==========================================================================================================

; ���������λ��
Func MyMouseClick($window, $text, $x, $y, $button = "Main", $clicks = "1" )
	$pos = WinGetPos($window, $text) 
	MouseClick($button, $x + $pos[0], $y + $pos[1], $clicks)
EndFunc

; �ƶ����λ��
Func MyMouseMove($window, $text, $x, $y)
	$pos = WinGetPos($window, $text) 
	MouseMove($x + $pos[0], $y + $pos[1])
EndFunc

; ��ק���λ��
Func MyMouseClickDrag($window, $text, $x1, $y1, $x2, $y2)
	$pos = WinGetPos($window, $text) 
	MouseClickDrag("Main", $x1 + $pos[0], $y1 + $pos[1], $x2 + $pos[0], $y2 + $pos[1])
EndFunc

; ����ָ������: 
Func MyScreenCapture($PicName, $window, $text)
	$pos = WinGetPos($window, $text) 
	_ScreenCapture_Capture($PicName, $pos[0], $pos[1], $pos[0] + $pos[2], $pos[1] + $pos[3])
EndFunc

; �������
Func start($path, $username, $password, $ip, $epNum)
	ShellExecute($path)														;������
	WinWait("�û���¼")														;�ȴ���¼����
	WinActivate("�û���¼")
	ControlSetText("�û���¼", "", "[CLASS:Edit; INSTANCE:1]", $username)	;�����û���
	ControlSetText("�û���¼", "", "[CLASS:Edit; INSTANCE:2]", $password)	;��������
	ControlSetText("�û���¼", "", "[CLASS:Edit; INSTANCE:3]", $ip)			;���÷�������ַ
	ControlFocus("�û���¼","","[CLASS:Button; INSTANCE:1]")				;����ƶ�����¼��ť
	ControlClick("�û���¼","","[CLASS:Button; INSTANCE:1]")				;�����¼
	Sleep(1000)
	WinWaitActive("", "lbComboBox", 10)										;�ȴ�ѡ����ҵ����,10�볬ʱ
	If WinExists("", "lbComboBox") Then												;���˺�ֻ��һ����ҵ�򲻻ᵯ���˿�
		ControlFocus("","lbComboBox","[CLASS:AfxWnd110u; INSTANCE:1]")		;����ƶ���ѡ���
		ControlClick("","lbComboBox","[CLASS:AfxWnd110u; INSTANCE:1]")		;���ѡ����ҵ��
		MyMouseClick("", "lbComboBox", 98, 138  + 26 * ($epNum - 1))		;ѡ���$epNum����ҵ
		ControlFocus("","","[CLASS:Button; INSTANCE:1]")					;����ƶ���ȷ��
		ControlClick("","","[CLASS:Button; INSTANCE:1]")					;���ȷ��
	EndIf
EndFunc

; �򿪹���
Func OpenProject($projTree)
	MyMouseClick($title, "", 113, 87)										;����򿪹���
	WinWaitActive("ѡ�񹤳�")
	If ControlTreeView ( "ѡ�񹤳�", "", "[CLASS:SysTreeView32; INSTANCE:1]", "Exists", $projTree) = 1 Then		;�жϽڵ��Ƿ����
		ControlTreeView ( "ѡ�񹤳�", "", "[CLASS:SysTreeView32; INSTANCE:1]", "Select", $projTree )			;���ڵ������ѡ��ڵ�
		MyMouseClick("ѡ�񹤳�", "", 170, 70, "Main", "2")								;˫����һ�����̣���һ���Ǳ�ѡ����
		WinWait("����״̬", "����", 10)
		If WinExists("����״̬", "����") Then WinWaitClose("����״̬", "����")
	Else
		MsgBox(0,"��ʾ", $projTree &"�ڵ㲻���ڣ�")						;���ڵ㲻��������ʾ
	EndIf
EndFunc

