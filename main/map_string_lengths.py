"""
Program:               map_string_lengths.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-09-08

Creates a list of lists of strings and their lengths via the map function.
"""


def get_string_and_string_length_list(string):
    """
    Gets a list of given string and its length.

    :param string: input string
    :return: list of input string and its length
    """
    return [string, len(string)]


if __name__ == '__main__':
    # Create list of ten strings
    string_list = ['Arch Linux', 'Artix Linux', 'Garuda Linux', 'Void Linux', 'Gentoo Linux', 'Debian GNU/Linux', 'NixOS', 'Kali Linux', 'FreeBSD', 'OpenBSD']

    # Use map function with get_string_and_string_length_list function and string_list list.
    string_and_string_length_list = list(map(get_string_and_string_length_list, string_list))

    # Print string_and_string_length_list.
    for string_and_string_length in string_and_string_length_list[:-1]:
        print(string_and_string_length[1], end=", ")
    print(string_and_string_length_list[-1][1])
