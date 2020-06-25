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
        url=settings.API_URL,
        json={'host': host, 'info': server_info})


def get_server_list():
    response = requests.get(
        url=settings.API_URL, )

    if not response.json()['status']:
        print('获取服务器列表失败！！！')

    return response.json()['data']


def run():
    pool = ThreadPoolExecutor(10)
    server_list = get_server_list()
    for server in server_list:
        pool.submit(task, server['hostname'])


if __name__ == '__main__':
    run()
