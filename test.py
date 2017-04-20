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


if __name__ == '__main__':
    unittest.main()

