"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    
    for item in items:
        print(item)

def get_all_evens(nums):
    
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

def get_odd_indices(items):
    result =[]
    for idx , value in enumerate(items):
        if idx % 2 != 0:
            result.append(value)
    return result


def print_as_numbered_list(items):
    i =1
    for item in items:
        print (f'{i}. {item}')
        i += 1

def get_range(start, stop):
    nums = list(range(start, stop))
    return nums

def censor_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_word = ""
    for letter in word:
        if letter in vowels:
           new_word += "*"
        else:
           new_word += letter
    return new_word

print(censor_vowels("hello"))

def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper() + word[1:])
    
    return ''.join(camel_case)

print(snake_to_camel("hello_world"))

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
