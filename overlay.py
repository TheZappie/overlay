from typing import Iterable

from shapely import STRtree, unary_union
from shapely.geometry.base import BaseGeometry


def overlay(geometries: Iterable[BaseGeometry]):
    """First features will be underneath, last feature on top"""
    result = []
    s = set()
    tree = STRtree(geometries)
    for idx, current_feature in enumerate(geometries):
        s.add(idx)
        overlapping_features = tree.geometries.take(list(set(tree.query(current_feature)) - s))
        cut = current_feature.difference(unary_union(overlapping_features))
        result.append(cut)
    return result
