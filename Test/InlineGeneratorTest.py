#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 下午9:05
# @Author  : Hou Rong
# @Site    : 
# @File    : InlineGeneratorTest.py
# @Software: PyCharm
import unittest
from toolbox.InlineGenerator import inline_generators, _from


class TestInlineGenerator(unittest.TestCase):
    def test_inline_generator(self):
        @inline_generators
        def outer(x):
            def inner_inner(x):
                for x in range(1, x + 1):
                    yield x

            def inner(x):
                for x in range(1, x + 1):
                    yield _from(inner_inner(x))

            for x in range(1, x + 1):
                yield _from(inner(x))

        result = []
        for x in outer(3):
            result.append(x)

        self.assertListEqual(result, [1, 1, 1, 2, 1, 1, 2, 1, 2, 3])
