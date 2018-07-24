from time import sleep
import autoit


def addfile():
	sleep(2)
	if autoit.win_exists('打开文件'):
		autoit.win_active('打开文件')
		autoit.mouse_click(x=780, y=50)
		autoit.send(r'C:\Users\Administrator\Desktop\Word文档')
		autoit.send('{ENTER}')
		autoit.mouse_click(x=780, y=970)
		autoit.send('2018.2.28收到文档---反馈复测-20170308-徐莘伟.docx')
		autoit.send('!o')
		sleep(2)
	else:
		raise Exception('没有打开文件窗口')	

if __name__ == '__main__':
	addfile()