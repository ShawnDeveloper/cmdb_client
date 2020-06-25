import paramiko
import settings
import requests
from concurrent.futures import ThreadPoolExecutor
from lib.plugins import get_server_info


# 远程执行命令
def ssh(hostname, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, password=settings.SSH_PWD)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read().decode('utf-8')
    ssh.close()
    return result.strip('\n')


def task(host):
    server_info = get_server_info(ssh, host)
    requests.post(
        url='http://127.0.0.1:8000/api/get_data/',
        json={'host': host, 'info': server_info})


def get_server_list():
    response = requests.get(
        url='http://127.0.0.1:8000/api/get_server_list/', )

    if not response.json()['status']:
        print('获取服务器列表失败！！！')

    return response.json()['data']


def run():
    pool = ThreadPoolExecutor(10)
    host_list = get_server_list()
    for host in host_list:
        pool.submit(task, host)


if __name__ == '__main__':
    run()
