import types

def list_object_to_list_dict(list_obj):

    result_list = []

    for lo in list_obj:
        result_list.append(object_to_dict(lo))

    return result_list

def object_to_dict(obj):

    result = {}

    attrs = [a for a in dir(obj) if not a.startswith('__')]
    for a in attrs:
        if (type(obj[a]) == types.InstanceType):
            result[a] = object_to_dict(obj[a])
        elif (type(obj[a]) == types.ListType):
            result[a] = list_object_to_list_dict(obj[a])
        else:
            result[a] = obj[a]

    return result
