#!/usr/bin/env python

"""Tests for `pyquote` package."""
from pyquote.pyquote import generate_quote
def test_return_is_dict():
    quote_dict=generate_quote()
    assert  isinstance(quote_dict, dict)
    assert {'Author','Quote'}==set(quote_dict.keys())