#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 下午9:04
# @Author  : Hou Rong
# @Site    : 
# @File    : InlineGenerator.py
# @Software: PyCharm
import types


def inline_generators(fn):
    def inline(value):
        if isinstance(value, InlineGenerator):
            for x in value.wrapped:
                for y in inline(x):
                    yield y
        else:
            yield value

    def wrapped(*args, **kwargs):
        result = fn(*args, **kwargs)
        if isinstance(result, types.GeneratorType):
            result = inline(_from(result))
        return result

    return wrapped


class InlineGenerator(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped


def _from(value):
    assert isinstance(value, types.GeneratorType)
    return InlineGenerator(value)
