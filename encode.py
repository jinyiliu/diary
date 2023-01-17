""" 参考《别怕，我们的聊天消息，没人能偷看》 """
import sys, os, rsa, base64

fn = sys.argv[1]

# 读取信息
with open(fn, 'r') as f:
    msg = f.read()

# 公钥
with open('key_rsa.public', 'r') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read().encode())

# 加密
def encrypt(msg, public_key):
    msg_bytes = msg.encode()
    encryptd_msg = b''
    chunk_size = len(msg_bytes) // 117 + 1 # 分块加密
    for chunk_index in range(chunk_size + 1):
        chunk = msg_bytes[chunk_index * 117: (chunk_index + 1) * 117]
        encryptd_msg += rsa.encrypt(chunk, public_key)
    encryptd_msg_str = base64.b64encode(encryptd_msg).decode()
    return encryptd_msg_str

encryptd_msg_str = encrypt(msg, public_key)

# 替换原文件
os.remove(fn)
with open(fn,'w') as f:
    f.write(encryptd_msg_str)
