# WordCounter

The `worlds_counter.py` module provides a `WordCounter` class for counting the occurrences of each word in a text file. 

Create an instance of this class by passing the path to the desired text file to the constructor, and then use the methods `get_count_to_std_out()`, `get_count()`, and `count_to_file(output_file)` to get the word count in the console, as a Python dictionary, or to write it to a specified text file, respectively.

```console
$python
...
>>> word_counter = WordCounter('path/to/file')
>>> word_counter.get_count_to_std_out()
1 lorem
1 ipsum
```

To run the tests, enter the command:
```bash
python tests.py
```