import logging 

log = logging.getLogger(__name__)

def dict_comparer(dict1, dict2, path="", dict1_name="dict1", dict2_name="dict2"):
    """
    deep compares two dictionaries and returns the differences as a dictionary
    Args:
        dict1:
        dict2:
        suffix: empty by default, used for recursive calls to pass in key path
        dict1_name: name of the first dictionary (used in return dictionary)
        dict2_name: name of the first dictionary (used in return dictionary)

    Returns: difference in the two dictionary in the format:
    {".path.to.key": {"dict1_name": "difference_val", "dict2_name": "difference2_val"}}
    if the sub dictionary is inside a list of the same length between the two dictionaries,
    it is of the following format with index
    {".path.to.list[index].key.difference": {"dict1_name": "difference_val", "dict2_name": "difference2_val"}}
    """
    keys = set(dict1.keys() + dict2.keys())
    res = {}
    for key in keys:
        new_key = "{}.{}".format(path, key)
        # if both values are dictionaries
        if dict1.get(key) and dict2.get(key) and \
                        type(dict1[key]) == dict and type(dict2[key]) == dict:
            res.update(dict_comparer(dict1[key], dict2[key], path=new_key,
                                     dict1_name=dict1_name, dict2_name=dict2_name))
        # if both values are list
        else:
            res.update(comparer(dict1.get(key), dict2.get(key), path=new_key,
                                     dict1_name=dict1_name, dict2_name=dict2_name))
    return res


def list_comparer(list1, list2, path="", dict1_name="dict1", dict2_name="dict2"):
    """
    compare two lists, return difference in dict format, helper for comparer
    Args:
        list1:
        list2:
        path:
        dict1_name:
        dict2_name:

    Returns:

    """
    res = {}
    # if the length of list is different, print difference
    if len(list1) != len(list2):
        res.update({path: {
            dict1_name: [x for x in list1 if x not in list2],
            dict2_name: [x for x in list2 if x not in list1]}})
    # list have same length
    else:
        for i in range(len(list1)):
            res.update(comparer(list1[i], list2[i], path="{}[{}]".format(path, i),
                                        dict1_name=dict1_name, dict2_name=dict2_name))   
    return res

def other_comparer(elem1, elem2, path="", dict1_name="dict1", dict2_name="dict2"):
    """
    literal comparison of two elements, returns the difference in a dictionary
    Args:
        dict1:
        dict2:
        suffix: empty by default, used for recursive calls to pass in key path
        dict1_name: name of the first dictionary (used in return dictionary)
        dict2_name: name of the first dictionary (used in return dictionary)
    """
    res = {}
    if elem1 != elem2:
        res.update({path: {dict1_name: elem1, dict2_name: elem2}})
    return res

def comparer(elem1, elem2, path="", dict1_name="dict1", dict2_name="dict2"):
    """
    deep compares two json objects and returns the differences as a dictionary
    json objects are dictionaries, lists, etc, that can be returned by json.loads()

    Args:
        elem1: first json object 
        elem2:
        suffix: empty by default, used for recursive calls to pass in key path
        dict1_name: name of the first dictionary (used in return dictionary)
        dict2_name: name of the first dictionary (used in return dictionary)

    Returns: difference in the two dictionary in the format:
    {".path.to.key": {"dict1_name": "difference_val", "dict2_name": "difference2_val"}}
    if the sub dictionary is inside a list of the same length between the two dictionaries,
    it is of the following format with index
    {".path.to.list[index].key.difference": {"dict1_name": "difference_val", "dict2_name": "difference2_val"}}
    """
    log.debug("comparing %s and %s" % (elem1, elem2))
    res = {}
    if type(elem1) == dict and type(elem2) == dict:
        log.debug("using dict comparer")
        res.update(dict_comparer(elem1, elem2, path=path, dict1_name=dict1_name, dict2_name=dict2_name))
    elif type(elem1) == list and type(elem2) == list:
        log.debug("using list comparer")
        res.update(list_comparer(elem1, elem2, path=path, dict1_name=dict1_name, dict2_name=dict2_name))
    else:
        log.debug("using other comparer")
        res.update(other_comparer(elem1, elem2, path=path, dict1_name=dict1_name, dict2_name=dict2_name))
    return res

