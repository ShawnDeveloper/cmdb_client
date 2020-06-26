import traceback

from .base import BasePlugin
from lib.utils.log import logger
from lib.utils.response import BaseResponse
from lib.utils import convert


class MemoryPlugin(BasePlugin):
    '''
    采集内存信息
    '''

    def process(self, ssh, hostname):
        response = BaseResponse()
        try:
            result = ssh(hostname, "free | awk 'NR>1{print $0}'")
            # result = ssh(hostname, 'dmidecode -q -t 17 2> /dev/null')
            response.data = self.parse(result)
        except Exception as e:
            logger.error(traceback.format_exc())
            response.status = False
            response.error = traceback.format_exc()

        return response.dict

    # def parse(self,content):
    #     ram_dict = {}
    #     key_map = {
    #         'Size':'capacity',
    #         'Locator':'slot',
    #         'Type':'model',
    #         'Speed':'speed',
    #         'Manufacturer':'manufacturer',
    #         'Serial Number':'sn'
    #     }
    #     devices = content.split('Memory Device')
    #     for item in devices:
    #         item = item.strip()
    #         if not item:
    #             continue
    #         if item.startswith('#'):
    #             continue
    #         segment = {}
    #         lines = item.split('\n\t')
    #         for line in lines:
    #             if len(line.split(':'))>1:
    #                 key,value = line.split(':')
    #             else:
    #                 key = line.split(':')[0]
    #                 value = ''
    #             if key in key_map:
    #                 if key == 'Size':
    #                     segment[key_map['Size']] = convert.convert_mb_to_gb(value,0)
    #                 else:
    #                     segment[key_map[key.strip()]] = value.strip()
    #         ram_dict[segment['slot']] = segment
    #
    #     return ram_dict

    def parse(self, content):
        meminfo_items = content.split('\n')
        meminfo_dic = {}
        for item in meminfo_items:
            cols = item.split()
            key = cols[0].replace(':', '')
            val_dic = {
                'total': cols[1],
                'used': cols[2],
                'free': cols[3],
            }

            if key == 'Mem':
                val_dic['shared'] = cols[4]
                val_dic['buff_cache'] = cols[5]
                val_dic['available'] = cols[6]

            meminfo_dic[key] = val_dic
        return meminfo_dic
