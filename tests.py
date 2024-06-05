import unittest
from unittest.mock import call
import tempfile
import unittest.mock
from words_counter import WordCounter

class TestWordCounter(unittest.TestCase):

    @unittest.mock.patch('builtins.print')
    def test_positive_stdout(self, print_mock):
        with tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8',delete_on_close=True) as file:
            content = 'Lorem ipsum dolor ipsum lorem'
            file.write(content)
            file.flush()

            word_counter = WordCounter(file.name)
            word_counter.get_count_to_std_out()
            expected = [call('2 lorem'),call('2 ipsum'), call('1 dolor')]
            
            print_mock.assert_has_calls(expected, any_order=False) 


    @unittest.mock.patch('builtins.print')
    def test_negative_std_out_no_such_file(self, mock_print):
        word_counter = WordCounter('nonexisting_file')
        word_counter.get_count_to_std_out()
        mock_print.assert_called_once_with(('You have to pass correct filename to WordCounter constructor. '\
                                            'File have to be at the same directory, or use full path.'))
        

    def test_positive_get_count_as_dict(self):
        with tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8',delete_on_close=True) as file:
            content = 'Lorem ipsum dolor ipsum lorem'
            file.write(content)
            file.flush()

            word_counter = WordCounter(file.name)
            result = word_counter.get_count()
            expected = {'lorem': 2, 'ipsum': 2, 'dolor': 1}

            self.assertDictEqual(result, expected)


    @unittest.mock.patch('builtins.open')
    def test_positive_writing_to_file(self, mock_open_arg):
        mock_input_file = unittest.mock.mock_open(read_data='Lorem lorem ipsum')
        mock_output_file = unittest.mock.mock_open()

        mock_open_arg.side_effect = [mock_input_file.return_value, mock_output_file.return_value]

        input_file_path = 'input.txt'
        output_file_path = 'output.txt'

        word_counter = WordCounter(input_file_path)
        word_counter.count_to_file(output_file_path)
      
        mock_open_arg.assert_any_call(input_file_path, 'r')
        mock_open_arg.assert_any_call(output_file_path, 'w+')

        mock_input_file().read.assert_called_once()

        mock_output_file().write.assert_called_once_with('2 lorem\n1 ipsum')



if __name__ == '__main__':
    unittest.main()




