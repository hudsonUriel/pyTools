# Universal Base Converter
# ************************************** #
# This library allows convert numbers
# to different bases
#
# The conversion process is made through
# the isomorphic relation between the
# individual aliases of an input string
# with an defined DECODE_ARRAY
#
# ************************************** #
# This tool is licensed under MIT terms.
#
# Be free to:
# [+] run
# [+] study
# [+] change
# [+] improve
# [+] redistribute
# [+] share
# [+] use commercially and privately
#
# ************************************** #

# import
from math import log

# generic decoding string
DECODE_ARRAY = '0123456789abcdefghijklmnopqrstuvwxy'


# defines
def convert(value_origin, base_origin, base_destiny):
    """
        This function makes the conversion of a
        value_origin number/chain written in a base_origin
        to a base_destiny, returning an list.

        ***** Function Arguments *****
        VALUE_ORIGIN  --> string or integer
        BASE_ORIGIN   --> integer
        BASE_DESTINY  --> integer

        ***** Function Return *****
        DESTINY --> list

        ***** e.g. *****

        VALUE_ORIGIN = 100101
        BASE_ORIGIN  = 2
        BASE_DESTINY = 10

        DESTINY = convert(VALUE_ORIGIN, BASE_ORIGIN, BASE_DESTINY)

        DESTINY = [3, 7]
        ..............................

        VALUE_ORIGIN = '1f5'
        BASE_ORIGIN  = 16
        BASE_DESTINY = 2

        DESTINY = convert(VALUE_ORIGIN, BASE_ORIGIN, BASE_DESTINY)

        DESTINY = [1, 1, 1, 1, 1, 0, 1, 0, 1]

        ..............................

        VALUE_ORIGIN = '5l2'
        BASE_ORIGIN  = 20
        BASE_DESTINY = 5

        DESTINY = convert(VALUE_ORIGIN, BASE_ORIGIN, BASE_DESTINY)

        DESTINY = [3, 4, 1, 4, 2]
    """
    value_origin = decode(str(value_origin), base_origin)

    destiny = []

    # calculates k
    k_origin = int(log(value_origin, base_destiny)) + 1

    # convert to base_destiny
    for i in range(1, k_origin + 1):
        # calculates potency and rest (mod)
        pot = base_destiny ** i
        rest = value_origin % pot
        rest /= base_destiny ** (i - 1)

        # appends
        destiny.append(int(rest))

        # updates value
        value_origin -= rest

    # reverse and returns
    destiny.reverse()
    return destiny


def convert_num(value_origin, base_origin, base_destiny):
    """
        This function makes the conversion of a
        value_origin number/chain written in a base_origin
        to a base_destiny, returning an string

        ***** Function Arguments *****
        VALUE_ORIGIN  --> string or integer
        BASE_ORIGIN   --> integer
        BASE_DESTINY  --> integer

        ***** Function Return *****
        DESTINY --> list

        ***** e.g. *****

        VALUE_ORIGIN = 100101
        BASE_ORIGIN  = 2
        BASE_DESTINY = 10

        DESTINY = convert_num(VALUE_ORIGIN, BASE_ORIGIN, BASE_DESTINY)

        DESTINY = 37
        ..............................

        VALUE_ORIGIN = '1f5'
        BASE_ORIGIN  = 16
        BASE_DESTINY = 2

        DESTINY = convert_num(VALUE_ORIGIN, BASE_ORIGIN, BASE_DESTINY)

        DESTINY = 111110101

        ..............................

        VALUE_ORIGIN = '5l2'
        BASE_ORIGIN  = 20
        BASE_DESTINY = 5

        DESTINY = convert_num(VALUE_ORIGIN, BASE_ORIGIN, BASE_DESTINY)

        DESTINY = 34142
    """

    return encode(
        convert(value_origin, base_origin, base_destiny)
    )


def decode(string_origin, base_destiny):
    """
        This function makes the isomorphic conversion
        of an chain in a base-10 number

        ***** Function Arguments *****
        STRING_ORIGIN  --> string or integer
        BASE_DESTINY  --> integer

        ***** Function Return *****
        DECODED --> integer

        ***** e.g. *****

        VALUE_ORIGIN = '22g'
        BASE_ORIGIN  = 18

        DECODED = decode(VALUE_ORIGIN, BASE_ORIGIN)

        DESTINY = 700
    """

    decoded = 0

    for i in range(len(string_origin)):
        decoded += (DECODE_ARRAY.index(string_origin[i])) \
                    * (base_destiny ** (len(string_origin) - (i+1)))

    return decoded


def encode(array):
    """
        This function makes the decode of an convert(...) operation
        to a string, using the DECODE_ARRAY

        ***** Function Arguments *****
        ARRAY  --> list

        ***** Function Return *****
        ENCODED --> string
    """

    encoded = ""
    for i in range(len(array)):
        encoded += DECODE_ARRAY[array[i]]

    return encoded


def set_decode_array(string):
    """
        Sets the DECODE_ARRAY.
        The default DECODE_ARRAY is the string:
        '0123456789abcdefghijklmnopqrstuvwxy'

        ***** Function Arguments *****
        STRING  --> string
    """

    DECODE_ARRAY = string