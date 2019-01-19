# -*- coding: utf-8 -*-
import keras


def main():
    file = open("input.txt", "r", 8192, "utf-8")
    text = file.read()
    print(text)


if __name__ == '__main__':
    main()
