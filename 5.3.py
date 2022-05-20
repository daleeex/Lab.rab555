#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__' :
    s1 = list('прроцесор')
    del s1[1]
    s1.insert(-2, 'с')
    print(*s1, sep='')
    
    s2 = list('теекстовыйфайл')
    del s2[1]
    s2.insert(-4, ' ')
    print(*s2, sep='')
    
    s3 = list('програма и аллгоритм')
    del s3[-7]
    s3.insert(6, 'м')
    print(*s3, sep='')
    
    s4 = list('процесор и паммять')
    del s4[-4]
    s4.insert(5, 'с')
    print(*s4, sep='')