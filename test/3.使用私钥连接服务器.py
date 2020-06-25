import paramiko
# 在当前机器使用 ssh-keygen 生成私钥和公钥，使用 ssh-copy-id 将公钥上传到服务器 ~/.ssh/authorized_keys 中
# 私钥文件路径
private_key_path = 'C:/Users/Administrator/.ssh/id_rsa'
# 读取私钥文件生成私钥对象
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# 创建 SSH 对象
ssh = paramiko.SSHClient()
# 允许连接不在 know_hosts 文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器，使用 key_filename 指定私钥路径
# ssh.connect(hostname='10.0.1.200', port=22, username='root', key_filename=private_key_path)
# 直接指定私钥对象
ssh.connect(hostname='10.0.1.200', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('hostname')
# 获取命令结果
result = stdout.read().decode()
# 打印结果
print(result)

# 关闭连接
ssh.close()