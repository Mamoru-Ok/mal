from utils import _input

def _read(_string):
    return _string

def _print(obj_read):
    print(obj_read)

def main():
    while True:
        try:
            obj_input = _input() 
            obj_read = _read(obj_input;)
            _print(obj_read)
        except EOFError:
            pass

if __name__ == "__main__":
    main()