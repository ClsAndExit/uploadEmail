# coding:utf-8
#@Time    :2019/3/31 15:56
import imaplib
import email
from email.header import decode_header
from util.file_toolkit import *
ConfigManager.init_class("config/emailFile.conf")

def decode_str(str_in):
    value, charset = decode_header(str_in)[0]
    if charset:
        value = value.decode(charset)
    return value

def get_att(msg_in):
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


def runing():
    user = ConfigManager.get_email_username()
    password = ConfigManager.get_email_password()
    server = ConfigManager.get_email_imapserver()
    conn = imaplib.IMAP4_SSL(server, 993)
    conn.login(user,password)
    #指定文件夹，这里指定收信箱
    conn.select('INBOX',readonly=True)
    #指定要读取的邮件的类型，"ALL" -- 所有邮件；"Recent" --- 未读
    type,data = conn.search(None,'ALL')
    for num in data[0].split()[::-1]:
        typ, data = conn.fetch(num, "(RFC822)")
        message = email.message_from_string(data[0][1].decode('utf-8'))
        get_att(message)

