#Region ;**** 参数创建于 ACNWrapper_GUI ****
#PRE_Res_requestedExecutionLevel=None
#EndRegion ;**** 参数创建于 ACNWrapper_GUI ****
#include <Public.au3>


Opt("MouseClickDelay", 50) ;鼠标延迟50毫秒点击
Opt("SendKeyDelay", 10) ;输入文本延迟10毫秒

;配置文件在读取时，需要填写绝对位置，否则是在Python脚本中无法识别的
Global $title = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "title",  "NotFound")
$IMtitle = IniRead("E:\TestAutomation\IM_test\autoit\BEcivil\mainConfig.ini", "parameters", "IMtitle",  "NotFound")
;$path = "D:\FTP下载包解压\bm_2.0.0_x64_release_2017-12-20_14-15\shell\PDSShell.exe"
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

;初始化进程
If ProcessExists($process_shell) Then ProcessClose($process_shell)
If ProcessExists($process_client) Then ProcessClose($process_client)
;If ProcessExists($process_co) Then ProcessClose($process_co)
If ProcessExists($process_IM) Then ProcessClose($process_IM)
If ProcessExists($process_ZYDL) Then ProcessClose($process_ZYDL)
WinActivate($title)
;启动BE市政
start($path, $username, $password, $ip, $epNum)
WinWaitActive($title, "", 60)
;WinWait("Luban Cooperation", "Chrom Legacy Window", 30)
;WinClose("Luban Cooperation")
;ProcessClose($process_coas)
WinActivate($title)
WinSetState($title, "", @SW_MAXIMIZE)