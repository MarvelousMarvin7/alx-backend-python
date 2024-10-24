#!/usr/bin/env python3
"""Annotation example"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """"return list"""
    return [(i, len(i)) for i in lst]
