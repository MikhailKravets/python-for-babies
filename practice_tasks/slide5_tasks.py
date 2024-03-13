from typing import Any


def init_key(d: dict[str, int], key: str, default_value: int = 0):
    d[key] = default_value


def concat_dicts(d1: dict[Any, Any], d2: dict[Any, Any]) -> dict[Any, Any]:
    """_summary_

    Args:
        d1 (dict[Any, Any]): _description_
        d2 (dict[Any, Any]): _description_

    Returns:
        dict[Any, Any]: _description_
    """
    # d1.update(d2)
    d3 = dict(d1)
    d4 = dict(d2)
    d3.update(d4)
    # d3 = {k: v for k, v in d1.items()}
    # d3.update(d4)
    return d3


if __name__ == "__main__":
    # Dictionary
    # Hash Map
    # Map
    counter = {"key": 0}
    init_key(counter, "two")
    init_key(counter, "three", 3)

    l = [v / 2 for v in range(0, 10_000, 2)]

    print(concat_dicts({1: 2, 3: 3}, {50: 1, 56: 2}))
