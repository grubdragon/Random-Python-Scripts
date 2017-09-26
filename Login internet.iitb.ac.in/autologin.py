import requests
payload = {'uname': '<YOUR USERNAME HERE>', 'passwd': '<YOUR PASSWORD HERE>'}
url = 'https://internet.iitb.ac.in/index.php'
requests.post(url, data=payload)
