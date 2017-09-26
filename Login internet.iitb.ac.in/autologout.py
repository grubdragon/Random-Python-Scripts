import requests
payload = {'button':'Logout'}
url = 'https://internet.iitb.ac.in/logout.php'
requests.post(url,payload)
