#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__' :
    s = input('Введите предложение: ')
    sub = 'нн'
    pos = -2
    while True:
        pos = s.find(sub, pos+2)
        if pos == -1:
            break
        print(s[pos:pos + 2])