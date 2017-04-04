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

	dict_3 = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

	dict_4 = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup_2"
                }
            }
        }
    }
}

	def setUp(self):
		pass

	def test_diffs(self):
		res = comparer(self.dict_1, self.dict_2)
		assert res[".key4"] == {'dict1': 'val4', 'dict2': 'val5'}, "first level diff not caught %s" % res[".key4"]
		assert res[".key5.key52"] == {'dict1': 'val52', 'dict2': 'val53'}, "second level diff not caught %s" % res[".key5.key52"]
		assert res[".key5.key52"] == {'dict1': 'val52', 'dict2': 'val53'}, "second level diff not caught %s" % res[".key5.key52"]
		assert res[".key6[1].k11"] == {'dict1': 'v11', 'dict2': 'v12'}, "second level diff not caught %s" % res[".key6[1].k11"]


	def test_no_incorrect_diffs(self):
		res = comparer(self.dict_1, self.dict_2)
		if len(res) != 3:
			assert False, "incorrect values in the dictionary %s" % res

	def test_larger_dict(self):
		res = comparer(self.dict_3, self.dict_4)
		assert res == {'.glossary.GlossDiv.GlossList.GlossEntry.GlossSee': {'dict1': 'markup', 'dict2': 'markup_2'}} , "bigger dictionary failure %s " % res

if __name__ == '__main__':
    unittest.main()
