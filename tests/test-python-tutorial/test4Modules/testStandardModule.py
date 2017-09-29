import __builtin__

def testBuildIn():
  buildInArr = dir(__builtin__)
  assert 'len' in buildInArr
  assert 'str' in buildInArr
