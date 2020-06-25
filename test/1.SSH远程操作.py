import paramiko

# 创建 SSH 对象
ssh = paramiko.SSHClient()
# 允许连接不在 know_hosts 文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.1.200', port=22, username='root', password='root1234')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('hostname')
# 获取命令结果
result = stdout.read().decode()
# 输出
print(result)
# 关闭连接
ssh.close()

'''执行结果：
    test-01
'''