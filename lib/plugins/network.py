import traceback

from .base import BasePlugin
from lib.utils.log import logger
from lib.utils.response import BaseResponse


class NetworkPlugin(BasePlugin):
    '''
    采集网络信息
    '''

    def process(self, ssh, hostname):
        response = BaseResponse()
        try:
            result = ssh(hostname, "ifconfig | grep 'inet ' -B1")
            response.data = self.parse(result)
        except Exception as e:
            logger.error(traceback.format_exc())
            response.status = False
            response.error = traceback.format_exc()

        return response.dict

    def parse(self, content):
        result = {}
        iface_str_list = content.split('--')
        for iface_str in iface_str_list:
            iface_name = iface_str[0:iface_str.find(':')].strip()
            iface_info = iface_str.strip().split('\n')[1]
            item_list = iface_info.split()
            info_dic = {
                'iface_name': iface_name,
                'ip': item_list[1],
                'netmask': item_list[3],
            }
            if len(item_list) == 6:
                info_dic['broadcast'] = item_list[5]
            result[iface_name] = info_dic

        return result
