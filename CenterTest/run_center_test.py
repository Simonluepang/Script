from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib, unittest, time, os
# 如果不加这个绝对路径的话，会造成page模块找不到base模块，具体原因为两个文件夹已经不是父子关系造成的
# 所以暂时只能先这样，后面如果想到好的办法了在进行改进
import sys
sys.path.append(r'F:\pythondemo\Github\Python-script\CenterTest\center\test_case\page_obj')


# ==========定义发送邮件===========
def send_mail(file_new):

	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()

	'''
	msg = MIMEText(mail_body, 'html', 'utf-8')
	msg = MIMEText('自动化测试报告详见附件。','plain','utf-8')
	msg['Subject'] = Header("Report",'utf-8')

	msg['from'] = 'xushenweitest@126.com'
	msg['to'] = '13939201399@163.com'

	smtp = smtplib.SMTP()
	smtp.connect("smtp.126.com")
	smtp.login("xushenweitest@126.com", "xu13939201399")
	smtp.sendmail("xushenweitest@126.com","13939201399@163.com", msg.as_string())
	smtp.quit()
	print('email has send out!')
	'''
	# 找到最新的测试报告
	sendfile = open(file_new, 'rb').read()

	# 
	att = MIMEText(sendfile, 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment; filename="report.html"'


	# 上传测试报告附件
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = Header("Report",'utf-8')	# 主题不能有test字样，否则会被认为是垃圾邮件
	msgRoot.attach(att)

	msgRoot['from'] = 'xushenweitest@126.com'
	msgRoot['to'] = '13939201399@163.com'

	smtp = smtplib.SMTP()
	smtp.connect("smtp.126.com")
	smtp.login("xushenweitest@126.com", "xu13939201399")
	smtp.sendmail("xushenweitest@126.com","13939201399@163.com", msgRoot.as_string())
	smtp.quit()
	print('email has send out!')
	


# ==========查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
	file_new = os.path.join(testreport, lists[-1])
	print(file_new)
	return file_new


if __name__ == '__main__':
	
	discover = unittest.defaultTestLoader.discover('./center/test_case', pattern='test_*.py')
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './center/report/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp, title='Center自动化测试报告', description='环境：Windows7-64x 浏览器：Chrome')
	runner.run(discover)
	fp.close()
	
	#file_path = new_report('./center/report')

	#send_mail(file_path)
	