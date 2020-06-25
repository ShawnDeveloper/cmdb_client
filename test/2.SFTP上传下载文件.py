import paramiko

transport = paramiko.Transport(('10.0.1.200', 22))
transport.connect(username='root', password='root1234')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将当前目录的 test_ssh.py 上传至服务器 /tmp/test_ssh.py
sftp.put('./test_ssh.py', '/tmp/test_ssh.py')
# 将服务器的 /tmp/test_ssh.py 下载到本地当前目录并命名为 test_ssh_download.py
sftp.get('/tmp/test_ssh.py', './test_ssh_download.py')

transport.close()