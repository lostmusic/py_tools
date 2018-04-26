#!/usr/bin/python
# coding:utf-8
import urllib2,cookielib,json
from flask import Flask,request
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/') #设置路由，可通过http://0.0.0.0:5000/来访问
def hello_world():

    return 'Hello World!'
@app.route('/projects/')
def projects():
    return "the project page"

@app.route('/username/<usernam>') #设置传入变量，可通过url请求来发送
def username(usernam):
    return "the username is:%s" % usernam

@app.route('/about')
def haha():
    return "the about page"

@app.route('/login',methods=['GET','POST']) #设置请求方式，get、post、put、delete等
def login():
    cookiejr = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookiejr)
    cookie_oppener = urllib2.build_opener(cookie_handler)
    urllib2.install_opener(cookie_oppener)
    send_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36',
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
    }
    login_url = "http://xxx.xxx.xxx/nauth/logincheck"
    
    #request.form.get("key", type=str, default=None) 获取表单数据
    #request.args.get("key") 获取get请求参数
    #request.values.get("key") 获取所有参数
    get_data = request.get_json() #获取请求post的json内容
    login_data = json.dumps(
        {"orgName": "app", "username": get_data["username"], "password": get_data["pwd"], "remember": 0, "hash": "",
         "scene": "", "token": "", "spectacle": ""})
    login_req = urllib2.Request(url=login_url,data=login_data,headers=send_header)
    login_req.get_method = lambda :"POST"
    login_res = urllib2.urlopen(login_req)
    if request.method == 'POST':
        feapp_url = 'http://xxx.xxx.xxx/home/feapp'
        feapp_req = urllib2.Request(url=feapp_url)
        feapp_req.get_method = lambda: "GET"
        feapp_res = urllib2.urlopen(feapp_req)
        jwt_str = BeautifulSoup(feapp_res, "lxml").find(class_="get-full-body").find_all("script")[1].text
        jwt = jwt_str.split('"')[1]

        return "JWT %s" % jwt
    elif request.method == 'GET':
        return "login sucessful"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
