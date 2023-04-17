"""
Test_Merge_Dicts:
How to use the script?
Run test in test classes with pytest with
pytest -q merge_dicts_test.py
"""

sphinx_needs_test_spec = ''
"""
.. test_spec:: Test of merge_dicts
   :id: TS_MERGE_DICTS
   :status: accepted

   This is a test specification for the module : need : `todo`.

   **Test Design**
   We create shapes, add them in the manager and calculate the total area.
"""

import sys
import os
sys.path.append(os.path.abspath('..'))
from merge_dicts import merge_dicts
import pytest

class Test_Merge_Dicts:
    def test_merge_dictionaries(self):
        print('1. It shall be possible to merge dictionaries.')
        a = {
            'a': 1,
            'b': 2,
            'c': 3,
            }
        #print(a)
        b = {
            'x': 4,
            'y': 5,
            'z': 6,
            }
        #print(b)
        [c, merge_conflict] = merge_dicts(a,b)
        #print(c)
        #print(merge_conflict)
        
        assert len(c) == 6
        assert ~merge_conflict

    def test_merge_dictionaries_different_content(self):
        print('2. If we have the same key in two dictinaries but different content,'+
              'the merge_conflict bit shall be set.')
        a = {
            'a': 1,
            'b': 2,
            'c': 3,
            }
        #print(a)
        d = {
            'x': 4,
            'b': 5, # b is now double defined with different value
            'z': 6,
            }
        #print(d)
        [e, merge_conflict] = merge_dicts(a,d)
        #print(e)
        #print(merge_conflict)
        
        assert len(e) == 5
        assert merge_conflict

    def test_merge_dictionaries_double_defined_content(self):
        print('3. If we have the same key in two dictinaries and the same content,'+
          'the merge_conflict bit shall not be set.')
        a = {
            'a': 1,
            'b': 2,
            'c': 3,
            }
        #print(a)
        f = {
            'x': 5,
            'b': 2, # b is now double defined with same value
            'z': 6,
            }
        #print(f)
        [g, merge_conflict] = merge_dicts(a,f)
        #print(g)
        #print(merge_conflict)
        
        assert len(g) == 5
        assert ~merge_conflict

    def test_merge_dictionaries_no_dict_exception(self):
        print('4. If we put in something else than a list of dictionaries,'+
              'we shall get an "AttributeError" excpetion.')
        h = ['a','b', 'c',]
        i = ['x','y', 'z',]
        
        with pytest.raises(AttributeError):
            [j, merge_conflict] = merge_dicts(h,i)

    def test_merge_empty_dictionaries(self):
        print('5. It shall be possible to give in empty dictionaries.')
        k = {}
        #print(k)
        [l, merge_conflict] = merge_dicts(k)
        #print(l)
        #print(merge_conflict)
        
        assert len(l) == 0
        assert ~merge_conflict

    def test_merge_dictionaries_no_parameter(self):
        print('6. It shall be possible to give nothing to the function')
        
        [m, merge_conflict] = merge_dicts()
        #print(l)
        #print(merge_conflict)
        
        assert len(m) == 0
        assert ~merge_conflict

    def test_merge_dictionaries_latest_defined_value_in(self):
        print('7. If we have the same key in two dictinaries but different content,'+
              'the first value shall be in the final dict.')
        a = {
            'a': 1,
            'b': 2,
            'c': 3,
            }
        #print(a)
        n = {
            'x': 4,
            'b': 5, # b is now double defined with different value
            'z': 6,
            }
        #print(n)
        [o, merge_conflict] = merge_dicts(a,n)
        #print(o)
        #print(merge_conflict)
        
        assert len(o) == 5
        assert o['b'] == 2
        assert merge_conflict

    def test_merge_many_dictionaries(self):
        print('8. It shall be possible to give in more than two dictinaries.')
        a = {
            'a': 1,
            'b': 2,
            'c': 3,
            }
        #print(a)
        p = {
            'l': 4,
            'm': 5,
            'n': 6,
            }
        #print(p)
        q = {
            'x': 7,
            'y': 8,
            'z': 9,
            }
        #print(q)
        [r, merge_conflict] = merge_dicts(a, p, q, )
        #print(r)
        #print(merge_conflict)
        
        assert len(r) == 9
        assert ~merge_conflict

