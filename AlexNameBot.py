# -*- coding: utf-8 -*-
import markovify


def main():
    file = open("input2.txt", "r", 8192, "utf-8")
    text = file.read()
    text_model = markovify.Text(text)
    print(text_model.make_sentence(tries=200))


if __name__ == '__main__':
    main()
