
from cmath import exp

import pytest

import translator.johnny_translator as jt


def test_read_content_from_string():
    content_string = "TAKE 1\nADD 2\nSUB 3"
    expected_output = ['TAKE 1', 'ADD 2', 'SUB 3']
    assert jt.read_content(content_string=content_string) == expected_output

def test_transform_assembler_content():
    content_string = """TAKE 1
                        ADD 2
                        SUB 3
                        """
    expected_output = "TAKE 1\nADD 2\nSUB 3"
    assert jt.transform_assembler_content(content_string=content_string) == expected_output

def test_transform_assembler_content_with_comments():
    content_string ="""TAKE 1 ;Comment 1
ADD 2 ;Comment 2
                    """
    expected_output ="""TAKE 1 ;Comment 1
ADD 2 ;Comment 2
                    """
    actual_output = jt.transform_assembler_content(content_string=content_string)
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {actual_output}")
    expected_output = expected_output.rstrip()
    assert jt.transform_assembler_content(content_string=content_string) == expected_output

#check if it moves variables correctly
def test_transform_assembler_content_with_defines():
    content_string ="""#define var1 1
#define var2 12
TAKE 1 ;Comment 1
ADD 2 ;Comment 2
                    """
    expected_output ="""TAKE 1 ;Comment 1
ADD 2 ;Comment 2
0
0
0
0
0
0
0
0
#define var1 1
#define var2 12
                    """
    actual_output = jt.transform_assembler_content(content_string=content_string)
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {actual_output}")
    expected_output = expected_output.rstrip()
    assert jt.transform_assembler_content(content_string=content_string) == expected_output


def test_transform_assembler_content_with_labels():
    content_string ="""loop1:
TAKE 1
ADD 2
JUMP loop1
                    """
    expected_output ="""TAKE 1
ADD 2
JUMP 0
                    """
    actual_output = jt.transform_assembler_content(content_string=content_string)
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {actual_output}")
    expected_output = expected_output.rstrip()
    assert jt.transform_assembler_content(content_string=content_string) == expected_output

def test_transform_assembler_content_with_labels_and_comments():
    content_string ="""loop1:      ;comment0
TAKE 1 ;comment1
ADD 2 ;comment2
JUMP loop1
loop2: ;comment3
ADD 3 ;comment4
                    """
    expected_output ="""TAKE 1 ;comment1
ADD 2 ;comment2
JUMP 0
ADD 3 ;comment4
                    """
    actual_output = jt.transform_assembler_content(content_string=content_string)
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {actual_output}")
    expected_output = expected_output.rstrip()
    assert jt.transform_assembler_content(content_string=content_string) == expected_output

