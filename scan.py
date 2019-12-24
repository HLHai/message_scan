import requests
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool
import optparse,sys
url_e=[]
end=[]
urls=[]
with open('url.txt','r') as f:
	for i in f.readlines():
		urls.append(i.strip())
print ("url加载成功>>>>>>>>>>>>")
def banner():
	print(
r'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
scan 源码泄露 tools
author：王嘟嘟
__________         __      __                           .___        .___     
\______   \___.__./  \    /  \_____    ____    ____   __| _/_ __  __| _/_ __ 
 |    |  _<   |  |\   \/\/   /\__  \  /    \  / ___\ / __ |  |  \/ __ |  |  \
 |    |   \\___  | \        /  / __ \|   |  \/ /_/  > /_/ |  |  / /_/ |  |  /
 |______  // ____|  \__/\  /  (____  /___|  /\___  /\____ |____/\____ |____/ 
        \/ \/            \/        \/     \//_____/      \/          \/      
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
''')

def scan(url):
	try:
		requests.adapters.DEFAULT_RETRIES = 5  
		url1=url+"王嘟嘟"
		html=requests.get(url=url1,headers={'User-Agent':UserAgent().random},timeout=5).text
		url1_content=len(html)
		html=requests.get(url=url,headers={'User-Agent':UserAgent().random},timeout=5)
		if url1_content==len(html.text) :
			return
		if html.status_code==200 and len(html.text)>0:
			print("[+] "+url)
			end.append(url)
	except Exception as e:
		pass


if __name__ == '__main__':
	banner()
	for url in urls:
		if(url.find("http")==-1 and url.find("https")==-1):
				print("[+] url不完整,进行填充");
				url="http://"+url
		if(url[-1:]=='/'):
			url=url[0:-1]
		with open("read1.txt",'r') as f:
			for i in f.readlines():
				i=i.strip()
				if (i[:1]!='/'):
					i='/'+i
				url_e.append(url+i)
		pool=Pool(50)
		result=pool.map(scan,url_e)
		pool.close()
	with open ('end.txt','a') as f:
		str=""
		for i in end:
			str+=i+'\n'
		f.write(str)
	print(len(end))	