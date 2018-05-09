import sys
import pytest 

sys.path.insert(0,'..')

from product.university import *


def test_sort_name():
	test = ["suong", "an", "nghia", "huynh"]
	assert sort_stu(test) == ["an", "huynh", "nghia", "suong"]