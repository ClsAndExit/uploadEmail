# -*- coding: utf-8 -*-
#@Time    :2019/3/31 15:56
import poplib
import email
import datetime
import time
from email.parser import Parser
from email.header import decode_header
import telnetlib
from util.conf_toolkit import ConfigManager
from util.file_toolkit import *
ConfigManager.init_class("config/emailFile.conf")
local_file_path = ConfigManager.get_local_resource_folder()

def decode_str(str_in):
    value, charset = decode_header(str_in)[0]
    if charset:
        value = value.decode(charset)
    return value

def get_att(msg_in,str_day_in):
    attachment_files = []
    for part in msg_in.walk():
        # 获取附件名称类型
        file_name = part.get_filename()
        if file_name and is_file_of_excel(file_name):
            h = email.header.Header(file_name)
            # 对附件名称进行解码
            dh = email.header.decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:
                # 将附件名称可读化
                filename = decode_str(str(filename, dh[0][1]))
                print(filename)
                # filename = filename.encode("utf-8")
            # 下载附件
            data = part.get_payload(decode=True)
            # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
            att_file = open(local_file_path+ filename, 'wb')
            attachment_files.append(filename)
            att_file.write(data)  # 保存附件
            att_file.close()
    return attachment_files

def run_ing():
    # 输入邮件地址, 口令和POP3服务器地址:
    email_user = ConfigManager.get_email_username()
    # 此处密码是授权码,用于登录第三方邮件客户端
    password = ConfigManager.get_email_password()
    pop3_server = 'pop.163.com'
    # 日期赋值
    day = datetime.date.today()
    str_day = str(day).replace('-', '')
    print(str_day)
    # 连接到POP3服务器,有些邮箱服务器需要ssl加密，可以使用poplib.POP3_SSL
    try:
        telnetlib.Telnet('pop.163.com', 995)
        server = poplib.POP3_SSL(pop3_server, 995, timeout=10)
    except:
        time.sleep(5)
        server = poplib.POP3(pop3_server, 110, timeout=10)

    print(server.getwelcome().decode('utf-8'))
    # 身份认证:
    server.user(email_user)
    server.pass_(password)
    # 返回邮件数量和占用空间:
    print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    print(mails)
    index = len(mails)
    # 倒序遍历邮件
    for i in range(index, 0, -1):
    # 顺序遍历邮件
    #for i in range(1, index + 1):
        resp, lines, octets = server.retr(i)
        # lines存储了邮件的原始文本的每一行,
        # 邮件的原始文本:
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        # 解析邮件:
        msg = Parser().parsestr(msg_content)
        # 获取邮件时间,格式化收件时间
        date1 = time.strptime(msg.get("Date")[0:24], '%a, %d %b %Y %H:%M:%S')
        # 邮件时间格式转换
        date2 = time.strftime("%Y%m%d", date1)
        if date2 < str_day:
            # 倒叙用break
            # break
            # 顺叙用continue
            continue
        elif date2 == str_day:
            # 获取附件
            file_name = get_att(msg, str_day)
            del_file_as_excel(file_name)
    server.quit()
