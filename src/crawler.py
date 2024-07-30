import re
import os
import requests
import configparser

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)

# 检查配置文件中是否存在 Authorization
if 'Authorization' not in config['DEFAULT']:
    print("配置文件中缺少 'Authorization' 键")
    authorization = os.getenv('Authorization')
else:
    authorization = config['DEFAULT']['Authorization']

def fetch_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Authorization": authorization,
        "X-Timeout": "30",
        "X-With-Generated-Alt": "true",
        "X-Target-Selector": "#img-content",
        "X-No-Cache": "true"
    }
    
    baseurl="https://r.jina.ai/" + url

    response = requests.get(
        baseurl,
        headers=headers
    )
    content = response.text
   
    return content

def get_title(content):
    match = re.search(r"Title:\s*(.*?)\s*URL", content)
    if match:
        title = match.group(1)
        return title
    return None