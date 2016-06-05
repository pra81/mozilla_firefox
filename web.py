#!/usr/bin/env python

import webbrowser
import time

url_facebook = "http://www.facebook.com"
url_gmail = "http://mail.google.com"
url_yahoomail = "http://mail.yahoo.co.in"
url_twitter = "http://twitter.com"
url_timesofindia = "http://timesofindia.indiatimes.com"
url_tuxmachines = "http://tuxmachines.org"
url_linuxtoday = "http://www.linuxtoday.com"

webbrowser.open_new(url_facebook)

time.sleep(15)

webbrowser.open_new_tab(url_gmail)

time.sleep(2)

webbrowser.open_new_tab(url_yahoomail)

time.sleep(2)

webbrowser.open_new_tab(url_twitter)

time.sleep(2)

webbrowser.open_new_tab(url_timesofindia)

time.sleep(2)

webbrowser.open_new_tab(url_tuxmachines)

time.sleep(2)

webbrowser.open_new_tab(url_linuxtoday)


