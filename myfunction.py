def get_request_type(dictionary):
    """
    リクエストタイプを取得する．

    Parameters
    ----------
    dictionary: dict
        payloadをdict型にエンコードしたもの．

    Returns
    ----------
    request_type: str
        リクエストタイプ．
    """
    request_type = ""
    try:
        request_type = dictionary["type"]
    except KeyError as e:
        print("catch KeyError: ", e)
    return request_type


def get_callback_id(dictionary, request_type):
    """
    コールバックIDを取得する．

    Parameters
    ----------
    dictionary: dict
        payloadをdict型にエンコードしたもの．
    request_type: str
        リクエストタイプ．

    Returns
    ----------
    callback_id: str
        コールバックID．
    """
    if request_type == "shortcut":
        callback_id = dictionary["callback_id"]
    elif request_type == "view_submission":
        callback_id = dictionary["view"]["callback_id"]
    else:
        callback_id = ""
    return callback_id
