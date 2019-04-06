# coding:utf-8
import re
import hashlib

def get_md5_id_from_str(url):
    md5 = hashlib.md5()
    if isinstance(url, str):
        md5.update(url.encode('utf-8'))
    elif isinstance(url, list):
        cat_url = ",".join(sorted(url))
        md5.update(cat_url.encode('utf-8'))
    else:
        raise ValueError("parameter must be str or list of str")
    return md5.hexdigest()

