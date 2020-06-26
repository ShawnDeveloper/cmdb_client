import traceback

from .base import BasePlugin
from lib.utils.log import logger
from lib.utils.response import BaseResponse


class BasicPlugin(BasePlugin):
    '''
    采集基础信息
    '''

    def process(self, ssh, hostname):
        response = BaseResponse()
        try:
            uname = ssh(hostname, 'uname').strip()
            version = ssh(hostname, 'cat /etc/redhat-release').strip().split('\n')[0]
            cpu_count = ssh(hostname, 'cat /proc/cpuinfo | grep "physical id" | uniq | wc -l ')
            kernel_version = ssh(hostname, 'uname -r')
            response.data = {
                'basic':
                    {
                        'uname': uname,
                        'version': version,
                        'cpu_count': cpu_count,
                        'kernel_version': kernel_version
                    }
            }
        except Exception as e:
            logger.error(traceback.format_exc())
            response.status = False
            response.error = traceback.format_exc()

        return response.dict
