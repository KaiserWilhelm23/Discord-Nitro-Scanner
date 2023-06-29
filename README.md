# Discord-Nitro-Scanner
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?business=2Q6R2RWPT7L6L&no_recurring=0&currency_code=USD)

# This is a working progress!!!! 

Currently there are issues with proxies and proxy rotation, this is used to bypass the rate limiter. 

Go to the newest release to download the EXE if you do not have python. 


# Proxy Rotation and User Agent Header Rotation: 

Proxy Rotate Code
```
url = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt"

response = requests.get(url)
proxy_list = response.text.strip().split('\n')

def rotate_proxies():
    proxy = random.choice(proxy_list)
    proxies = {'http': proxy, 'https': proxy}
    return proxies
```
User Agent Header Rotation Code

```
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'
]

def rotate_user_agents():
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}
    return headers


```

