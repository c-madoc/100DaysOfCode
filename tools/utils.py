# -*- coding: UTF-8 -*-
# -------------------------------------------------------------------------
# utils.py - Contains common tools and reusable functionality.
#
# Description:
# This module encapsulates functions that are used globally throughout
# a bot or sentinel instance; or plugins/cogs.
# -------------------------------------------------------------------------
import base64
import datetime
import math
import os
import random
import re
import string
from random import randint

import requests
from bs4 import BeautifulSoup as bs

class TextUtils:
    """Contains a collection of text formatting utilities such as random case conversion and making a input alphanumeric only."""

    @staticmethod
    def generate_id(length: int = 10) -> int:
        """Allows the creation of an alphanumeric string for sentinel identification."""
        characters = string.ascii_letters + string.digits
        result = ''.join((random.choice(characters) for i in range(length)))
        return result

    @staticmethod
    def escape_md(text: str) -> str:
        """
        Formats input so that any markdown tags are removed.
        :param text     : String to espace markdown from
        :return         : The escaped string
        """
        markdown = ['*', '`', '_', '~', '\\', '||']
        result = ""
        for c in text:
            if not c in markdown:
                result += c
        return result

    def alphabet(self: "TextUtils", text: str) -> str:
        """
        A function to filter a string to only allow alphabetical characters.
        :param text     : String to convert to alphabetical chars only
        :returns        : Formatted alphabetical string
        """
        pattern = re.compile('[^a-zA-Z]+')
        return pattern.sub('', text)

    def alphabet_and_spaces(self: "TextUtils", text: str) -> str:
        """
        A function to filter a string to only allow alphabetical characters and spaces.
        :param text     : String to convert to alphabetical chars and spaces only
        :returns        : Formatted alphbetical string with spaces
        """
        pattern = re.compile('[^a-zA-Z ]+')
        return pattern.sub('', text)

    def random_case(self: "TextUtils", text: str) -> str:
        """
        A function to convert a string to "random case".\n
        :param text     : String to convert to "random case"\n
        :returns        : Formatted string that's in "random case"
        """
        result = ''
        for index, character in enumerate(text, 1):
            if character == 'i' or index == 1:
                result += character.lower()
            else:
                integer = randint(0, 1)
                result += character.upper() if integer == 0 else character.lower()
        return result

    def has_links(self: "TextUtils", text: str) -> bool:
        """Determines if a message contains any links."""
        try:
            common_protocols = ['http', 'https', 'ftp', 'ssh', 'mailto', 'file', 'data', 'irc']
            result = re.search(
                r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",
                text).group(0)
            if result:
                for protocol in common_protocols:
                    if result.startswith(protocol):
                        return True
                    else:
                        pass
            else:
                return False
        except:
            return False


class FormatUtils:  # Will deal with a lot of text output for Discord messages and embeds.
    """Encapsulates a collection of formatting variables and functionality which make Discord output cleaner."""
    SYMBOLS = {
        'asterisk': '\u002A',
        'bullet': '\u2022',
        'hollow': '\u25E6',
        'hyphen': '\u2043',
        'triangle': '\u2023'
    }

    def split_args(self, args):
        return [x.strip() for x in args.split(',')]

    def _get_symbol(self: "FormatUtils", symbol: str) -> str:
        """
        A function to check for the existence of a specified symbol.
        :param symbol       : String to search for a symbol in
        :returns            : The symbol if one is found
        """
        if symbol in self.SYMBOLS and symbol is not None:
            symbol = self.SYMBOLS.get(symbol)
        return symbol

    def format_list(self: "FormatUtils", items: list, **kwargs) -> str:
        """
        A function to format a list, so it is readable when it is output to Discord.
        :param items        : A collection of strings to join in a nice list
        :param **kwargs     : A collection of arguments to the symbol from
        :returns            : A formatted string containing all the list items
        """
        sort = kwargs.get('sort')
        enums = kwargs.get('enumerate')
        symbol = kwargs.get('symbol')
        symbol = self._get_symbol(symbol)
        if sort:
            items = sorted(items)
        if enums:
            return '\n'.join(items)
        if symbol is not None:
            result = []
            for item in items:
                if symbol == '*':
                    result.append(f"{symbol}{item}")
                else:
                    result.append(f"{symbol} {item}")
            return '\n'.join(result)
        return ', '.join(items)

    def si_to_number(self, x):
        """Would take 100k and turn it into 1000000
        :param: x: 100k, 2m
        """
        total_stars = 0
        if 'k' in x:
            if len(x) > 1:
                total_stars = float(x.replace('k', '')) * 1000  # convert k to a thousand
        elif 'm' in x:
            if len(x) > 1:
                total_stars = float(x.replace('m', '')) * 1000000  # convert M to a million
        elif 'b' in x:
            total_stars = float(x.replace('b', '')) * 1000000000  # convert B to a Billion
        elif ',' in x:
            total_stars = float(x.replace(',', ''))  # removing ,
        else:
            total_stars = int(x)  # Less than 1000
        return int(total_stars)

    def human_format(self, num):
        """Takes in a large number and changes the output based on the
        example 100000 = 100k
        :param: num: 100000
        """
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        # add more suffixes if you need them
        return '%.2f%s' % (num, ['', 'K', 'M', 'B', 'T', 'P'][magnitude])


class ConversionUtils:
    """Contains a collection of tools that allow easier conversions of types and values."""

    def bool_to_int(self: "ConversionUtils", value: bool) -> int:
        """
        Converts a boolean value into a integer.
        :param value        : The boolean flag to convert
        :returns            : The integer value of the boolean
        """
        if value is True:
            return 1
        else:
            return 0

    def int_to_bool(self: "ConversionUtils", value: int) -> bool:
        """
        Converts a integer into a boolean value.
        :param value        : The integer value to convert
        :returns            : The boolean value of the integer
        """
        if value is None or value == 0:
            return False
        else:
            return True

    def decode_string_to_list(self, string: str, split_type: str) -> list:
        unparsed = str(base64.b64decode(string)).replace("b'", "").replace("'", "")
        decoded_list = unparsed.split(split_type)
        return decoded_list

    def decode_string_to_string(self, string):
        decoded = str(base64.b64decode(string)).replace("b'", "").replace("'", "")
        return decoded


class TimeUtils:
    """Encapsulates a variety of functions that make working with time and dates simpler."""

    def regex_check(self: "TimeUtils", text: str) -> bool:
        """Check if someone entered the correct time format: month, day, year, hour, and minutes.
        :param: check   : 2020 06 06 18 00
        :returns        : A flag indicating there was a match
        """
        if re.match(r"\d\d\s\d\d\s\d\d\d\d\s\d\d\s\d\d", text):
            return True
        else:
            return False

    def regexed_date(self: "TimeUtils", text: str) -> str:
        """Takes in a string and checks it based on month, day, year, hours and minutes.
        :param: date    : 06 06 2020 18 00
        :returns        : A formatted time string
        """
        date = str(text)
        check_date = re.compile(r'\d+')
        new_date = check_date.findall(date)
        month = new_date[0]
        day = new_date[1]
        year = new_date[2]
        hours = new_date[3]
        mins = new_date[4]
        seconds = new_date[5]
        new_date = f"{month}/{day}/{year} {hours}:{mins}:{seconds}"
        dt_object2 = datetime.strptime(str(new_date), "%Y/%m/%d %H:%M:%S")
        timestamp = datetime.timestamp(dt_object2)
        date_time = datetime.fromtimestamp(timestamp)
        return date_time.strftime("%c")

    def display_time(self, seconds: int, granularity=2) -> int:
        intervals = (
            ('weeks', 604800),  # 60 * 60 * 24 * 7
            ('days', 86400),  # 60 * 60 * 24
            ('hours', 3600),  # 60 * 60
            ('minutes', 60),
            ('seconds', 1),
        )

        result = []

        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return ', '.join(result[:granularity])


class SystemUtils:
    """Encapsulation of common operating system identifiers."""
    windows = "nt"
    linux = "posix"
    macos = "posix"
    cygwin = "posix"

    def get_system(self: "System") -> str:
        """Returns the name of the currently running operating system."""
        return os.name