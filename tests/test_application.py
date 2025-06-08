import pytest
from application.application import Application
# kjllk

app = Application()

class TestApplication:

	def test_math_operation_summation(self):
		assert app.math_operation_summation(5,2) == 6

	def test_math_operation_division(self):
		assert app.math_operation_division(10,2) == 5

	def test_math_operation_multiplicatioin(self):
		assert app.math_operation_multiplication(5,2) == 10

	def test_math_operation_substration(self):
		assert app.math_operation_subtraction(5,2) == 3

