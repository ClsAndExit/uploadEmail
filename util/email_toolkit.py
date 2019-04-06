# coding:utf-8
#@Time    :2019/3/31 15:56
import poplib
import imaplib
import email
import datetime
import time
from email.parser import Parser
from email.header import decode_header
import telnetlib
from util.conf_toolkit import ConfigManager
from util.file_toolkit import *
ConfigManager.init_class("config/emailFile.conf")

def decode_str(str_in):
    value, charset = decode_header(str_in)[0]
    if charset:
        value = value.decode(charset)
    return value

def get_att(msg_in,str_day_in):
    attachment_files = []
    for part in msg_in.walk():
        file_name = part.get_filename()
        if file_name:
            h = email.header.Header(file_name)
            # 对附件名称进行解码
            dh = email.header.decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:
                filename = decode_str(str(filename, dh[0][1]))
                print(filename)
                # filename = filename.encode("utf-8")
            #判断附件是否为excel文件
            if is_file_of_excel(filename):
                # 下载附件
                data = part.get_payload(decode=True)
                download_to_local_file(filename=filename,data=data)
                attachment_files.append(filename)

    return attachment_files

def pop_run_ing():
    email_user = ConfigManager.get_email_username()
    password = ConfigManager.get_email_password()
    pop3_server = ConfigManager.get_email_server()
    # 日期赋值
    day = datetime.date.today()
    str_day = str(day).replace('-', '')
    print(str_day)
    # 连接到POP3服务器,有些邮箱服务器需要ssl加密，可以使用poplib.POP3_SSL
    try:
        telnetlib.Telnet(pop3_server, 995)
        server = poplib.POP3_SSL(pop3_server, 995, timeout=10)
    except:
        time.sleep(5)
        server = poplib.POP3(pop3_server, 110, timeout=10)

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
    #将所有邮件先保存到list中防止连接失效
    all_email = list()
    for j in range(1,index+1):
        all_email.append(server.retr(j))
    # 倒序遍历邮件
    length_ = len(all_email)
    for i in range(length_-1, 0, -1):
        resp, lines, octets = all_email[i]
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
            # 获取附件
            file_name = get_att(msg, str_day)
            del_file_as_excel(file_name)
    server.quit()


def imap_run_ing():
    pass