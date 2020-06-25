def convert_to_int(value, defalut=0):
    try:
        result = int(value)
    except Exception as e:
        result = defalut

    return result


def convert_mb_to_gb(value, default=0):
    try:
        value = value.strip('MB')
        result = int(value)
    except Exception as e:
        result = default

    return result
