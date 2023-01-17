""" 参考《别怕，我们的聊天消息，没人能偷看》 """
import sys, os, rsa, base64

fn = sys.argv[1]

# 读取加密信息
with open(fn, 'r') as f:
    encryptd_msg_str = f.read()

# 私钥
with open('key_rsa.private', 'r') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read().encode())

# 解密
def decrypt(encryptd_msg, private_key):
    encryptd_msg = base64.b64decode(encryptd_msg_str.encode())
    chunk_size = len(encryptd_msg) // 128
    msg_bytes = b''
    for chunk_index in range(chunk_size):
        chunk = encryptd_msg[chunk_index * 128: (chunk_index + 1) * 128]
        msg_bytes += rsa.decrypt(chunk, private_key)
    return msg_bytes.decode()

print(decrypt(encryptd_msg_str, private_key))
