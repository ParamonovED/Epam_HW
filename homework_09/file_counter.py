"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>> > universal_file_counter(test_dir, "txt")
6
>> > universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    for sub_element in dir_path.iterdir():
        if sub_element.is_dir():
            counter += universal_file_counter(sub_element, file_extension, tokenizer)
        if str(sub_element).endswith(file_extension):
            counter += one_file_counter(f"{sub_element}", tokenizer)
    return counter


def one_file_counter(file_name: str, tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    if tokenizer is None:
        with open(file_name) as el:
            counter += len([1 for _ in el])
    else:
        with open(file_name) as el:
            counter += sum(len(tokenizer(line)) for line in el)
    return counter
