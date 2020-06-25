import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PLUGIN_CLASS_LIST = {
    'filesystem': 'lib.plugins.filesystem.FileSystemPlugin',
    'memory': 'lib.plugins.memory.MemoryPlugin',
    'network': 'lib.plugins.network.NetworkPlugin',
    'board': 'lib.plugins.board.BoardPlugin',
    'basic': 'lib.plugins.basic.BasicPlugin',
}

SSH_USER = 'root'
SSH_PORT = 22
SSH_PWD = 'root1234'

LOGGING_PATH = os.path.join(BASE_DIR, 'log/cmdb.log')

API_URL = 'http://127.0.0.1:8000/api/server/'
