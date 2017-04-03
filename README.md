# py-json-comparer
python json / dictionary comparer

Python module to compare two JSON objects and return diffs at the lowest possible level in a flattened dictionary with dot separated concanated keys as resulting key and both the values in a dictionary within it.  If the object are lists and are of the same length, the key has the index of the diff element and elements are further analyzed. 
JSON objects to be passed in can be dict, list, or the response of json.loads().

Usage: 


```python

from json_comparer.dict_comparer import comparer

json1 = {
        "key1": "val1",
        "key2": "val2",
        "key4": "val4",
        "key6": [{"k10": "v10"}, {"k11": "v11"}],
    }

json2 = {
        "key1": "val1",
        "key2": "val2",
        "key4": "val5",
        "key6": [{"k10": "v10"}, {"k11": "v12"}],
    }

print comparer(json1, json2, dict2_name="json1", dict1_name="json2")

#Result is:
#{'.key4': {'json2': 'val4', 'json1': 'val5'}, 
#   '.key6[1].k11': {'json2': 'v11', 'json1': 'v12'}}

```
