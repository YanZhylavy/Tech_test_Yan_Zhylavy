class WordCounter:
    '''
    Please pass the name of the file from which you want to read the text for word counting 
    to the WordCount constructor when creating the object. 
    It is recommended to use the full path to the file.
    Use methods get_count(), get_count_to_std_out() and
    count_to_file() to retrieve words count in different ways.

    '''
    def __init__(self, filename: str):
        self._counter = {}
        try:
            with open(filename, 'r') as f:
                all_words_list = f.read().split()
                for word in all_words_list:
                    word = word.lower()
                    if word not in self._counter:
                        self._counter[word] = 1
                    else:
                        self._counter[word] += 1 
        except FileNotFoundError:
            print(('You have to pass correct filename to WordCounter constructor. ' \
                   'File have to be at the same directory, or use full path.'))                


    def get_count_to_std_out(self) -> None:

        for word, count in self._counter.items():
            print(f'{count} {word}')  
            

    def get_count(self) -> dict:
        return self._counter    


    def count_to_file(self, output_file: str) -> None:
        with open(output_file, 'w+') as f:
            lines = [f'{count} {word}' for word, count in self._counter.items()]
            lines = '\n'.join(lines)
            f.write(lines)
        
                            