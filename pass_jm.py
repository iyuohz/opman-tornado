#!coding:utf-8
from passlib.hash import sha256_crypt

def pass_crypt(str):

    '对传入的字符串进行sha256加密'

    hash_pass = sha256_crypt.encrypt(str)
    return hash_pass

def pass_verify(str,db_pass):

    '解密'

    varify_pass = sha256_crypt.verify(str,db_pass)
    return varify_pass

