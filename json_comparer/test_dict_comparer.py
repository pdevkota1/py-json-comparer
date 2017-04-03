import unittest
from dict_comparer import comparer

class TestCompare(unittest.TestCase):

	dict_1 = {
        "key1": "val1",
        "key2": "val2",
        "key4": "val4",
        "key5": {"key51": "val51", "key52": "val52"},
        "key6": [{"k10": "v10"}, {"k11": "v11"}],
    }

	dict_2 = {
        "key1": "val1",
        "key2": "val2",
        "key4": "val5",
        "key5": {"key51": "val51", "key52": "val53"},
        "key6": [{"k10": "v10"}, {"k11": "v12"}],
    }

	def setUp(self):
		pass

	def test_diffs(self):
		res = comparer(self.dict_1, self.dict_2)
		assert(res[".key4"] == {"dict_1": "val4"}, {"dict_2": "val5"}, "first level diff not caught")
		assert(res[".key5.key52"] == {"dict_1": "val52"}, {"dict_2": "val53"}, "second level diff not caught")
		assert(res[".key5.key52"] == {"dict_1": "val52"}, {"dict_2": "val53"}, "second level diff not caught")
		assert(res[".key6[1].k11"] == {"dict_1": "val11"}, {"dict_2": "val12"}, "second level diff not caught")


	def test_no_incorrect_diffs(self):
		res = comparer(self.dict_1, self.dict_2)
		if len(res) != 3:
			assert (False, "incorrect values in the dictionary %s" % res)



if __name__ == '__main__':
    unittest.main()