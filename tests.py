import unittest
from unittest.mock import call
import tempfile
import unittest.mock
from words_counter import WordCounter

class TestWordCounter(unittest.TestCase):

    @unittest.mock.patch('builtins.print')
    def test_stdout(self, print_mock):
        with tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8',delete_on_close=True) as file:
            content = 'Lorem ipsum dolor ipsum lorem'
            file.write(content)
            file.flush()
            WordCounter.get_count_to_st_out(file.name)
            expected = [call('2 lorem'),call('2 ipsum'), call('1 dolor')]
            print_mock.assert_has_calls(expected, any_order=False)   


if __name__ == '__main__':
    unittest.main()




