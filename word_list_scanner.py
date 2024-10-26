import re
from dataclasses import dataclass
from typing import List

def scan_word_list(word_list: List[str], test_string: str) -> object:

    @dataclass
    class WordTestResult:
        in_list: bool
        test_string_len: int
        match_start: int
        match_end: int

    test_string_list = re.split(r'\s+', test_string)
    test_string_len = len(test_string_list)
    test_string_first_word = test_string_list[0]

    word_test_obj = WordTestResult(False, test_string_len, 0, 0)

    for word_index,word in enumerate(word_list):
        if word == test_string_first_word:
            
            sample_word_list = word_list[word_index:word_index+test_string_len]

            if sample_word_list == test_string_list:
                word_test_obj.in_list = True
                word_test_obj.match_start = word_index
                word_test_obj.match_end = word_index + test_string_len - 1
                break
    
    return word_test_obj