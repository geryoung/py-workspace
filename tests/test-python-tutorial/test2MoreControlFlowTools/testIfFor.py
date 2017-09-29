#! /use/bin/env python
# -*- coding: utf-8 -*-

def testFor():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        w += 't'
        print w, len(w)
    
    assert words[0] == 'catt'
    assert words[1] == 'windowt'
    assert words[2] == 'defenestratet'

def testFor2():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        w += 't'
        print w, len(w)
    
    assert words[0] == 'catt'
    assert words[1] == 'windowt'
    assert words[2] == 'defenestratet'

def testRange1():
    p = []
    p = range(10)
    assert p[5]==5
    assert p[1]==1
    assert p[9]==9

def testRange2():
    p = []
    p = range(10)
    assert p[1]==5
    assert p[2]==6
    assert p[3]==7


def testForAndRange():
    print ''
    assert 1==2


####################### 
# function test
#######################

def testDefFunc():
    print ''
    assert 1==2


def testDefFuncDefaultVal():
    print ''
    assert 1==2

def testDefFuncKeywordArgs():
    print ''
    assert 1==2

def testUnpackingArgsList():
    print ''
    assert 1==2

def testLambdaForm():
    def test1():
        return 1
    f = test1()
    assert f(1)==40
    assert f(2)==41