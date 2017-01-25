import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.start import start

start_instance = start()

class StartTestCases(unittest.TestCase):
  def test_checks_for_strings(self):
    word = 'yippee'
    self.assertEqual(
      start_instance.check_string(word),
      (word, "You have 6 letters in 'yippee'"),
      msg="String, '{}' not detected correctly".format(word)
    )

  def test_checks_for_single_string(self):
    word = 'a'
    self.assertEqual(
      start_instance.check_string(word),
      (word, "You have 1 letter in 'a'"),
      msg="String, '{}' not detected correctly".format(word)
    )

  def test_returns_error_for_emptystrings(self):
    word = ''
    self.assertEqual(
      start_instance.check_string(word),
      (word, "Stop annoying me with empty strings"),
      msg="Empty string, '{}' falsely detected".format(word)
    )

  def test_it_only_accepts_strings(self):
    with self.assertRaises(TypeError) as context:
      start_instance.check_string(2)
      self.assertEqual(
        'Argument should be a string',
        context.exception.message,
        'String inputs allowed only'
      )

unittest.main()