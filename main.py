from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    seen = {}
    for k, v in mapping.items():
        if v in seen:
            return (seen[v], k)
        seen[v] = k
    return None


def find_non_surjective_element(mapping: dict, target: set):
    range_set = set(mapping.values())
    for elem in target:
        if elem not in range_set:
            return elem
    return None


def my_floor(x: float) -> int:
    n = int(x)
    if x < 0 and x != n:
        return n - 1
    return n


def my_ceil(x: float) -> int:
    n = int(x)
    if x > 0 and x != n:
        return n + 1
    return n