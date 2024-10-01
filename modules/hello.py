import sys

def say_hello(name):
    print(f'Hello {name}')
def main():
    print('Y imported hello.py')
    say_hello('user')
for args in sys.argv:
    print(args)

if __name__ == '__main__':
    main()