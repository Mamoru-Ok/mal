import re
import traceback

from utils import _input, MalError

REAL_NUMBER_FMT = r"-?\d+(?:\.\d+)?"
STRING_FMT = r'"[^"\s]+"'
OTHER_FMT = r"[^\(\)\s]"
ATOM_FMT = r"(?:{}|{}|{})".format(REAL_NUMBER_FMT, STRING_FMT, OTHER_FMT)

MIDDLE_FMT = r"\s+"
SYMBOL_FMT = r"[^\(\)\s]+"
SIMPLE_HEAD_FMT = r"\s*(?:{}|{})".format(SYMBOL_FMT, ATOM_FMT)
SIMPLE_UNHEAD_FMT = r"(?:{}{})+\s*".format(MIDDLE_FMT, ATOM_FMT)
SIMPLE_LIST_FMT = r"\({0}{1}\)".format(SIMPLE_HEAD_FMT, SIMPLE_UNHEAD_FMT)

DATA_FMT = f"(?:{ATOM_FMT}|{SIMPLE_LIST_FMT})"
HEAD_FMT = r"\s*(?:{}|{})".format(SYMBOL_FMT, DATA_FMT)
UNHEAD_FMT = r"(?:{}{})+\s*".format(MIDDLE_FMT, DATA_FMT)
LIST_FMT = r"\({0}{1}\)".format(HEAD_FMT, UNHEAD_FMT)
LIST_P = re.compile(f"{LIST_FMT}|{ATOM_FMT}")


def _parse(_string):
    data = LIST_P.findall(_string)
    
    head_and_tail = _string[::len(_string) - 1]
    if "()" != head_and_tail and len(data) > 1:
        raise MalError("Not List")
    
    for idx, d in enumerate(data):
        if "()" == d[::len(d) - 1]:
            data[idx] = _parse(d)

    return data

def _read(_string):
    if not _string:
        raise MalError("Input is empty")
    
    ast = _parse(_string)
    return ast

def _merge(obj_read):
    for idx, d in enumerate(obj_read):
        if isinstance(d, list):
            obj_read[idx] = _merge(d)
    
    contents = " ".join(obj_read)
    return "({})".format(contents)

def _print(obj_read):
    print(_merge(obj_read))

def main():
    while True:
        try:
            obj_input = _input() 
            obj_read = _read(obj_input)
            _print(obj_read)
        except MalError:
            traceback.print_exc()
        except EOFError:
            break

if __name__ == "__main__":
    main()
