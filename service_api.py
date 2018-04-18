#!/usr/bin/python
# coding:utf-8
import cookielib,json
import urllib2
from bs4 import BeautifulSoup
from flask import Flask,request
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)

# class HelloWorld(flask_restful.Resource):
#     def get(self):
#         return {'hello': 'world'}

class jwt_message(flask_restful.Resource):
    def __init__(self):
        super(jwt_message, self).__init__()
        cookiejr = cookielib.CookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(cookiejr)
        cookie_oppener = urllib2.build_opener(cookie_handler)
        urllib2.install_opener(cookie_oppener)
        self.send_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36',
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
        }
    def post(self,todo_id):
        login_url = "http://app.shujushijue.cn/nauth/logincheck"
        todos = request.form["username"]
        # login_data = json.dumps({"orgName":"app","username":todos['username'],"password":todos['pwd'],"remember":0,"hash":"","scene":"","token":"","spectacle":""})
        # login_req = urllib2.Request(url=login_url,headers=self.send_header,data=login_data)
        # login_req.get_method = lambda :"POST"
        # urllib2.urlopen(login_req)
        # feapp_url = 'http://app.shujushijue.cn/home/feapp'
        # feapp_req = urllib2.Request(url=feapp_url)
        # feapp_req.get_method = lambda: "GET"
        # feapp_res = urllib2.urlopen(feapp_req)
        # jwt_str = BeautifulSoup(feapp_res, "lxml").find(class_="get-full-body").find_all("script")[1].text
        # jwt = jwt_str.split('"')[1]
        # return {"JWT %s" % jwt}
        return todos



# api.add_resource(HelloWorld, '/')
api.add_resource(jwt_message,'/<string:todo_id>')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
