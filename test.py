import unittest
import wordninja


class TestWordNinja(unittest.TestCase):

  def test_simple(self):
    self.assertEqual(list(wordninja.split('derekanderson')), ['derek','anderson'])

  def test_with_underscores_etc(self):
    self.assertEqual(list(wordninja.split('derek anderson')), ['derek','anderson'])
    self.assertEqual(list(wordninja.split('derek-anderson')), ['derek','anderson'])
    self.assertEqual(list(wordninja.split('derek_anderson')), ['derek','anderson'])
    self.assertEqual(list(wordninja.split('derek/anderson')), ['derek','anderson'])

  def test_caps(self):
    self.assertEqual(list(wordninja.split('DEREKANDERSON')), ['DEREK','ANDERSON'])

  def test_digits(self):
    self.assertEqual(list(wordninja.split('win32intel')), ['win','32','intel'])

  def test_apostrophes(self):
    self.assertEqual(list(wordninja.split("that'sthesheriff'sbadge")), ["that's","the","sheriff's","badge"])

if __name__ == '__main__':
    unittest.main()

