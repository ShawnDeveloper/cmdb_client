class BasePlugin(object):
    '''
    插件基类
    '''

    def process(self, ssh, hostname):
        raise NotImplementedError('{} 必须实现 process 方法'.format(self.__class__.__name__))
