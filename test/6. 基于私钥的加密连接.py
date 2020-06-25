import paramiko

# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('C:/Users/Administrator/.ssh/id_rsa')

# 创建一个通道
transport = paramiko.Transport(('10.0.1.200', 22))
transport.connect(username='root', pkey=private)

# 实例化 SSHClient
client = paramiko.SSHClient()
client._transport = transport

# 打开一个 Channel 并执行命令
stdin, stdout, stderr = client.exec_command('df -h')
# stdout 为正确输出，stderr 为错误输出，同时是有1个变量有值

# 打印执行结果
print(stdout.read().decode('utf-8'))

# 关闭 SSHClient
transport.close()
