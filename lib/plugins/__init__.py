import importlib
import settings

def get_server_info(ssh,hostname):
    server_info = {}
    for key, path in settings.PLUGIN_CLASS_LIST.items():
        module_path, class_name = path.rsplit('.', maxsplit=1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        plugin_obj = cls()
        info = plugin_obj.process(ssh,hostname)
        server_info[key] = info

    return server_info
