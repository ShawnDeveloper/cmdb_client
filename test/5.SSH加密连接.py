import paramiko

# 创建一个通道
transport = paramiko.Transport(('10.0.1.200', 22))
transport.connect(username='root', password='root1234')

# 实例化 SSHClient
ssh = paramiko.SSHClient()
ssh._transport = transport

# 打开一个 Channel 并执行命令
stdin, stdout, stderr = ssh.exec_command('hostname')

# 打印结果
print(stdout.read().decode('utf-8'))

# 关闭连接
transport.close()
