#coding=utf8
import requests,re,time

username = '用户名'
password = '密码' 
ID = '399'
check = 'vm'
restart = 'vm.restart'

checkurl = 'http://kvm.free-www.ru:1500/vmmgr?out=xml&authinfo={0}:{1}&func={2}&elid={3}'.format(username,password,check,ID)
keepurl = 'http://kvm.free-www.ru:1500/vmmgr?out=xml&authinfo={0}:{1}&func={2}&elid={3}'.format(username,password,restart,ID)
list1 = [('ok', 'vm.restart')]


def check(url = checkurl):
	try:
		s = requests.Session()
		r = s.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except Exception as e:
		print(e)

def restart(url = keepurl):
	try:
		s = requests.Session()
		r = s.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		khtml = r.text
		result = re.findall(r'><(.*)/><tparams><elid>237</elid><out>xml</out><func>(.*)</func>',khtml)
		if list1 == result:
			print("Success Runing!")
		else:
			print("Error")
	except Exception as e:
		print(e)	

def main():
	rhtml = check()
	state = re.findall(r'<vmstatus>(.*)</vmstatus>',rhtml)
	if "running" in state:
		print("free-www is Running")
	else:
		restart()

if __name__ == '__main__':
	while True:
		main()
		time.sleep(300)
