# tests/test_evaluator.py

import unittest
from interpreter import evaluate
from environment import Environment
from ast_tree import Number, BinOp, Assign, If

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.env = Environment()

    def test_number(self):
        node = Number(5)
        result = evaluate(node, self.env)
        self.assertEqual(result, 5)

    def test_binop_add(self):
        node = BinOp(Number(3), '+', Number(4))
        result = evaluate(node, self.env)
        self.assertEqual(result, 7)

    def test_binop_gt(self):
        node = BinOp('a', '>', Number(0))
        self.env.variables['a'] = 10
        result = evaluate(node, self.env)
        self.assertTrue(result)

    def test_assign(self):
        node = Assign('a', Number(10))
        result = evaluate(node, self.env)
        self.assertEqual(self.env.variables['a'], 10)
        self.assertEqual(result, 10)

    def test_if_true(self):
        assign = Assign('a', Number(10))
        evaluate(assign, self.env)
        condition = BinOp('a', '>', Number(5))
        body = [Assign('a', BinOp('a', '-', Number(5)))]
        if_node = If(condition, body)
        evaluate(if_node, self.env)
        self.assertEqual(self.env.variables['a'], 5)

    def test_if_false(self):
        assign = Assign('a', Number(3))
        evaluate(assign, self.env)
        condition = BinOp('a', '>', Number(5))
        body = [Assign('a', BinOp('a', '-', Number(5)))]
        if_node = If(condition, body)
        evaluate(if_node, self.env)
        self.assertEqual(self.env.variables['a'], 3)

    def test_undefined_variable(self):
        with self.assertRaises(Exception) as context:
            evaluate('b', self.env)
        self.assertIn("Undefined variable 'b'", str(context.exception))

    def test_division_by_zero(self):
        node = BinOp(Number(10), '/', Number(0))
        with self.assertRaises(ZeroDivisionError):
            evaluate(node, self.env)

if __name__ == '__main__':
    unittest.main()
