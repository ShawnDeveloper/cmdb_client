import traceback

try:
    int('aaa')
except Exception as e:
    print(traceback.format_exc())