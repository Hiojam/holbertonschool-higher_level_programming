#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = a // b
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(float(result)))
    return float(result)
