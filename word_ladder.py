#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

#    stack = []
#    stack.append(start_word)
#    q = []
#    q.append(stack)
#    with open(dictionary_file) as f:
#        words = f.readlines()
#    if len(start_word) != len(end_word):
#        return
#    elif start_word == end_word:
#        stack.append(end_word)
#        return stack
#    else:
#        while q != []:
#            q.pop(0)
#            for i in range(len(words)):
#                if _adjacent(words[i], stack[0]) == True:
#                    if words[i] == end_word:
#                        stack.append(words[i])
#                        return stack
#                    stack.copy()
#                    stack.append(words[i])
#                    q.append(stack)
#                    words.pop(i)
#            return

    stack = []
    stack.append(start_word)
    q = deque()
    q.append(stack)
    dictionary = open('words5.dict')
    words = dictionary.read().split("\n")
    if len(start_word) != len(end_word):
        return
    elif start_word == end_word:
        return stack
    else:
        while q:
            leftmost_stack = q.popleft()
            for wrd in set(words):
                if _adjacent(wrd, leftmost_stack[-1]):
                    if wrd == end_word:
                        leftmost_stack.append(wrd)
                        return leftmost_stack
                    stack_copy = copy.deepcopy(leftmost_stack)
                    stack_copy.append(wrd)
                    q.append(stack_copy)
                    words.remove(wrd)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    counter = 0
    if ladder == []:
        return False
    if len(ladder) == 1:
        return True
    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i + 1]):
            counter += 0
        else:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    counter = 0
    if word1 == word2:
        return False
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
        if counter == 1:
            return True
        else:
            return False
    else:
        return False
