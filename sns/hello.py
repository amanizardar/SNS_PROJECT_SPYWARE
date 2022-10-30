# import webbrowser

# url = 'http://docs.python.org/'

# # MacOS
# # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# # Windows
# # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# # Linux
# # chrome_path = '/usr/bin/google-chrome %s'

# # webbrowser.get(chrome_path).open(url)

# webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

import webbrowser

url = 'https://pythonexamples.org'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)

# import webbrowser

# url = 'https://pythonexamples.org'
# webbrowser.register('chrome',
# 	None,
# 	webbrowser.BackgroundBrowser("C://ProgramData//Microsoft//Windows//Start Menu//Programs//Google Chrome"))
# webbrowser.get('chrome').open_new(url)