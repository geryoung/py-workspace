# Methods of File Objects
# f.read()
# f.readline()



def testReadline():
  f = open('./data1.dat', 'r')
  line1 = f.readline()
  assert line1 == "testline1\n"
  line2 = f.readline()
  assert line2 == "testline2\n"

