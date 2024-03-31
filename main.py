# from definitions import *
import json


def test1():
    with open ("./parameters.json", "r") as param:
        data = json.load(param)
        print(f"{data}")
        print(type(data))
        for key in data:
            print(key)


def main():
    print("running test1\n")
    test1()


if __name__ == "__main__":
    main()
