#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__' :
    (lambda x: print(*filter(lambda y: y.isalpha() and x.count(y) == 1, x)))(''.join(input().lower() for _ in '123'))