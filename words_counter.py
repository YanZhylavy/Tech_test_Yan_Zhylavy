class WordCounter:

    @staticmethod
    def get_count_to_st_out(filename: str) -> None:
        counter = {}
        with open(filename, 'r') as f:
            all_words = f.read().split()
            for word in all_words:
                if word not in counter:
                    counter[word] = 1
                else:
                    counter[word] += 1 

        for words, counts in counter.items():
            print(f'{counts} {words}')              

WordCounter.get_count_to_st_out('testfile.txt')