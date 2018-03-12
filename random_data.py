#!/usr/bin/python
# encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import string,random
def phone_num(num):
    '''
    创建指定数量的随机手机号码
    :param num:手机号数量
    :return:手机号
    '''
    tel_num = []
    head_num = ["133","153","173","177","180","181","189","134","135","136",
                "137","138","139","150","151","152","157","158","159","178",
                "182","183","184","187","188","130","131","132","155","156","175","176","185","186","170","171"]
    for m in xrange(num):
        last_num = []
        for x in xrange(8):
            last_num.append(random.choice(string.digits))
        temp_num = random.choice(head_num) + ''.join(last_num)
        tel_num.append(temp_num)
    return tel_num

def random_mail(num):
    '''
    创建指令数量的随机邮件
    :param num:邮件数量
    :return: 邮件
    '''
    mail_output = []
    mail_end_str = {"国外常用":["@hotmail.com","@msn.com","@yahoo.com","@gmail.com","@aim.com","@aol.com","@mail.com","@walla.com","@inbox.com"],
                    "国内常用":["@126.com","@163.com","@sina.com","@21cn.com","@sohu.com","@yahoo.com.cn","@tom.com","@qq.com","@etang.com",
                            "@eyou.com","@56.com","@x.cn","@chinaren.com","@sogou.com","@citiz.com"],
                    "中国香港":["@hongkong.com","@ctimail.com","@hknet.com","@netvigator.com","@mail.hk.com","@swe.com.hk","@ITCCOLP.COM.HK","@BIZNETVIGATOR.COM"],
                    "中国台湾":["@SEED.NET.TW","@TOPMARKEPLG.COM.TW","@PCHOME.COM.TW"],
                    "巴基斯坦":["@cyber.net.pk"],"阿曼":["@omantel.net.om"],"意大利":["@ibero.it"],"南非":["@webmail.co.za"],
                    "新西兰":["@xtra.co.nz"],"新加坡":["@pacific.net.sg", "@FASTMAIL.FM"],
                    "美国":["@aol.com","@netzero.net","@twcny.rr.com","@comcast.net","@warwick.net","@comcast.net","@cs.com","@verizon.net"],
                    "其他":[]}
    mail_str = string.digits + string.letters
    for x in xrange(num):
        mail_country = random.choice(mail_end_str.keys())
        mail_start = "".join(random.sample(list(mail_str),12))
        if mail_country == "其他":
            mail_middle = ''.join(random.sample(mail_str,4))
            mail_hole = "%s@%s.com" % (mail_start, mail_middle)
        else:
            mail_middle = random.choice(mail_end_str[mail_country])
            mail_hole = mail_start + mail_middle
        mail_output.append(mail_hole)
    return mail_output


def random_str(len):
    '''
    创建一个指定长度的字符
    :param len:需求长度
    :return:字符串
    '''
    str_tmp = []
    for x in xrange(len):
        str_tmp.append(random.choice(string.letters))
    return ''.join(str_tmp)

def random_pu(len):
    '''
    创建一个指定长度的特殊字符
    :param len:
    :return:
    '''
    str_temp = []
    for x in xrange(len):
        str_temp.append(random.choice(string.punctuation))
    return ''.join(str_temp)

def random_str_dig(len):
    '''
    创建一个指定长度数字＋字母的字符
    :param len:
    :return:
    '''
    str_temp = []
    for x in xrange(len):
        if x%2 == 1:
            str_temp.append(random.choice(string.letters))
        else:
            str_temp.append(random.choice(string.digits))
    random.shuffle(str_temp)
    return ''.join(str_temp)

def random_str_dig_pu(len):
    '''
    创建一个指定长度数字＋字母＋特殊字符的字符
    :param len:
    :return:
    '''
    str_temp = []
    for x in xrange(len):
        if x%3 == 0:
            str_temp.append(random.choice(string.letters))
        elif x%3 ==1:
            str_temp.append(random.choice(string.punctuation))
        else:
            str_temp.append(random.choice(string.digits))
    random.shuffle(str_temp)
    return ''.join(str_temp)
