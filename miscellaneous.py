import requests

# *** Authentication and session manager
url = "https://api.github.com/user"
gh_respose = requests.get(url, auth=(
    'user_name_goes_here', 'password_goes_here'))
print(f"GitHub response is {gh_respose.status_code}")

se = requests.session()
se.auth = auth = ('user_name_goes_here', 'password_goes_here')
url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)


# *** sending cookies if required
cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshettyacademy.com',
                        allow_redirects=False, cookies=cookie, timeout=1)

print(response.history)
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'February'})
response = se.get('https://httpbin.org/cookies',
                  cookies={'visit-year': '2022'})
print(response.text)

# Attachments
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file': open('C:\\Users\\camsh\\OneDrive\\Pictures\\bg.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.status_code)
print(response.text)
