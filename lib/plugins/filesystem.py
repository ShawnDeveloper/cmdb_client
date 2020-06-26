import traceback

from .base import BasePlugin
from lib.utils.log import logger
from lib.utils.response import BaseResponse


class FileSystemPlugin(BasePlugin):
    '''
    采集硬盘信息
    '''

    def process(self, ssh, hostname):
        response = BaseResponse()
        try:
            info = ssh(hostname, 'df')
            response.data = self.parse(info)
        except Exception as xe:
            logger.error(traceback.format_exc())
            response.status = False
            response.error = traceback.format_exc()

        return response.dict

    def parse(self, info):
        result = {}
        key_map = {
            'Filesystem': 'fs',
            '1K-blocks': 'size',
            'Used': 'used',
            'Available': 'avail',
            'Use%': 'usage_rate',
            'Mounted': 'mounted',
        }
        info_list = info.split('\n')
        header_cols = info_list.pop(0).split()
        for row in info_list:
            cols = row.split()
            col_dic = {
                key_map[header_cols[0]]: cols[0],
                key_map[header_cols[1]]: cols[1],
                key_map[header_cols[2]]: cols[2],
                key_map[header_cols[3]]: cols[3],
                key_map[header_cols[4]]: cols[4].replace('%',''),
            }
            result[cols[5]] = col_dic
        return result
