#test_university.py

import pytest
# import sys
# import traceback
# sys.path.insert(0, '..' )


from product.university import sort_stu
from product.student import Student 


def test_sort():
	global list
	list = [Student("hoa"),Student("an"),Student("suong"),Student("nghia")]
	list = sort_stu(list)
	assert list[0].name == "an"
	assert list[3].name == "suong"
	
	
