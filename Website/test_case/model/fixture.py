import os


def filepath():
    file = os.path.dirname(__file__)
    base_file = os.path.dirname(os.path.dirname(os.path.dirname(file)))
    base = base_file.replace('\\', '/')
    base = str(base)
    return base




if __name__ == '__main__':
    filepath()
