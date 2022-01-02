import sys

def add(a,b):
    return a+b

def main(args):
    exit_code = 0
    print('hello, world')
    return exit_code

if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as e:
        print(e, file=sys.stderr)
