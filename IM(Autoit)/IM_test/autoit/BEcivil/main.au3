#Region ;**** ���������� ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** ���������� ACNWrapper_GUI ****
#include <Public.au3>


Opt("MouseClickDelay", 50) ;����ӳ�50������
Opt("SendKeyDelay", 10) ;�����ı��ӳ�10����

;�����ļ��ڶ�ȡʱ����Ҫ��д����λ�ã���������Python�ű����޷�ʶ���
Global $title = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "title",  "NotFound")
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "IMtitle",  "NotFound")
;$path = "D:\FTP���ذ���ѹ\bm_2.0.0_x64_release_2017-12-20_14-15\shell\PDSShell.exe"
$path = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "path",  "NotFound")
$process_shell = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "process_shell",  "NotFound")
$process_client = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "process_client",  "NotFound")
;$process_co = IniRead("mainConfig.ini", "parameters", "process_co",  "NotFound")
;$process_coas = IniRead("mainConfig.ini", "parameters", "process_coas",  "NotFound")
$process_IM = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "process_IM",  "NotFound")
$process_ZYDL = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "process_ZYDL",  "NotFound")
$username = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "username",  "NotFound")
$password = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "password",  "NotFound")
$ip = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "ip",  "NotFound")
$epNum = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "epNum",  "NotFound")


;WinActivate($title)

;��ʼ������
If ProcessExists($process_shell) Then ProcessClose($process_shell)
If ProcessExists($process_client) Then ProcessClose($process_client)
;If ProcessExists($process_co) Then ProcessClose($process_co)
If ProcessExists($process_IM) Then ProcessClose($process_IM)
If ProcessExists($process_ZYDL) Then ProcessClose($process_ZYDL)
WinActivate($title)
;����BE����
start($path, $username, $password, $ip, $epNum)
WinWaitActive($title, "", 60)
;WinWait("Luban Cooperation", "Chrom Legacy Window", 30)
;WinClose("Luban Cooperation")
;ProcessClose($process_coas)
WinActivate($title)
WinSetState($title, "", @SW_MAXIMIZE)