from pathlib import Path

BASE_DIR = Path(__file__).parent

if __name__ == '__main__':
    f = None

    try:
        f = open(BASE_DIR.joinpath('.static/one.txt'))
        print(f.read())
    except FileNotFoundError:
        print("File not found")
    else:
        print("close file")
        f.close()

    with open(BASE_DIR.joinpath('.static/one.txt')) as f:
        print(f.read())
    print(f.closed)
