import requests


def get_server_info(hostname, user='root', pwd='root1234'):
    import paramiko

    # 创建 SSH 对象
    ssh = paramiko.SSHClient()
    # 允许连接不在 know_hosts 文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='10.0.1.200', port=22, username=user, password=pwd)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('df -h | awk \'$NF=="/"{print $(NF-2)}\'')
    # 获取命令结果
    result = stdout.read().decode()
    # 关闭连接
    ssh.close()

    return result


def run():
    hostname = '10.0.1.200'
    info = get_server_info(hostname)

    # result = requests.get('http://127.0.0.1:8000/api/get_data/', params={'host': hostname, 'info': info})
    result = requests.post('http://127.0.0.1:8000/api/get_data/', json={'host': hostname, 'info': info.strip('\n')})

    print('把资产信息发送到 API', result.text)


if __name__ == '__main__':
    run()
