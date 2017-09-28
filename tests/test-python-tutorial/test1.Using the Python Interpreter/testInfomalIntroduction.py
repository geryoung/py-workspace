#! /usr/bin/env python
# -*- coding: utf-8 -*-

def testUnicodeString():
  print 'Hello\u7ED3\u7B97World !'
  print u'Hello\u7ED3\u7B97World !'
  print u"结算".encode('utf-8')
  print unicode("结算", "utf-8")


def testListSlice():
  p = [1,2,3,4]
  p[1:3] = []
  assert p == [1,4]

def testListInsert():
  p = [1,2,3,4]
  p1 = [1,2,3,4]
  p2 = [1,2,3,4]

  assert p == [1,2,5,6,3,4] #insert 
  assert p1 == [1,2,3,4,1,2,3,4] # copy
  assert p2 == [] # clear

def test