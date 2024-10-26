This is a basic Python application that checks a word or phrase against a list of words. 

The function accepts a list of strings and a string of one or more words. The test string is broken into a list by spaces. The test phrase is measured by word count, and the list of strings is checked to see if the test string exists.

The function returns a dataclass:

* in_list: boolean
* test_string_len: integer
* match_start: integer
* match_end: integer

I use this to search an email body for a test phrase. This allows me to categorize the email and find certain template values.

This is a single file application and uses only vanilla Python. No package dependencies at all.

