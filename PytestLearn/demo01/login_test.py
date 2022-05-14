import pytest
from PytestLearn.UnitClass.test_unit import Fun
class TestClass:
    def setup_class(self):
        print("setup_module:整个.py执行一次")

    def teardown_class(self):
        print("teardown_module：整个test_unit.py执行一次")

    def setup(self):
        print("setup_function:每个用例开始前都会执行")

    def teardown(self):
        print("teardown_function：每个用例结束后都会执行")

    @pytest.mark.parametrize("x,y,answer", [(1, 1, 2), (2, 2, 4)])
    def test_one(self,x,y,answer):
        # rec = Fun()
        assert Fun().funx(x, y) == answer
        # print("test_one")
    @pytest.mark.repeat(5)
    def test_answer(self):
        # rec = Fun()
        assert Fun().funx(1,0) == 1
        print("test_answer")

