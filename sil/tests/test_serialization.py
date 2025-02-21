""" Basic serialization/deserialization testing
 manipulating raw bytes without any typeinfo
 (intended to be used for RPC communication, as fast as possible)

 NOTE:  Annotations can include both python type and format
        per https://docs.python.org/3/library/struct.html#format-characters
        like some_fiend: Annotated[int, 'h']
        Library will check if python types correspond to format.

Skipped format implies following:
    - Python's int implies i (int)
    - Python's float implies d (double)


Formats per https://docs.python.org/3/library/struct.html#format-characters
including our mapping rules are as follows:

| Format | C Type             | Python type       | Standard | Notes    | our stdint.h
|        |                    |                   |   size   |          |    type
|--------|--------------------|-------------------|----------|----------|----------------------------
| x      | pad byte           | no value          |          | (7)      | uint8_t
| c      | char               | bytes of length 1 | 1        |          | char
|        |                    |                   |          |          | shall static assert sizeof(char) == 1
| b      | signed char        | integer           | 1        | (1), (2) | int8_t
| B      | unsigned char      | integer           | 1        | (2)      | uint8_t
| ?      | _Bool              | bool              | 1        | (1)      | bool stdbool.h or uint8_t
|        |                    |                   |          |          | shall static assert sizeof(bool) == 1
| h      | short              | integer           | 2        | (2)      | int16_t
| H      | unsigned short     | integer           | 2        | (2)      | uint16_t
| i      | int                | integer           | 4        | (2)      | int32_t
| I      | unsigned int       | integer           | 4        | (2)      | uint32_t
| l      | long               | integer           | 4        | (2)      | int32_t
| L      | unsigned long      | integer           | 4        | (2)      | uint32_t
| q      | long long          | integer           | 8        | (2)      | int64_t
| Q      | unsigned long long | integer           | 8        | (2)      | uint64_t
| n      | ssize_t            | integer           |          | (3)      | not allowed here (we always use <)
| N      | size_t             | integer           |          | (3)      | not allowed here (we always use <)
| e      | (6)                | float             | 2        | (4)      | (float)
| f      | float              | float             | 4        | (4)      | float
| d      | double             | float             | 8        | (4)      | double
| s      | char[]             | bytes             |          | (9)      | special case
| p      | char[]             | bytes             |          | (8)      | special case
| P      | void*              | integer           |          | (5)      | not allowed here

"""

import unittest
# from typing import get_type_hints
from typing import get_type_hints, cast, Any

from dataclasses import astuple
from typing import Annotated, Final

from devsure.rpc.serialization import serializable


# NOTE: all formats used below correspond to keys from FORMAT_TO_CPP

@serializable
class ClassWithFormats:
    """ To test all kinds of formats for serialization/deserialization """
    # NOTE1: padding here is just as sample and testing
    #        (no real use case intended here)
    # NOTE2: one must initialize "padding place" here,
    #        to not being forced to "initialize" padding in constructor
    field_pad_byte: Annotated[None, 'x']

    field_char: Annotated[bytes, 'c']  # char -> bytes of length 1
    field_signed_char: Annotated[int, 'b']  # signed char -> integer
    field_unsigned_char: Annotated[int, 'B']  # unsigned char -> integer
    field_bool: Annotated[bool, '?']  # _Bool -> bool
    field_short: Annotated[int, 'h']  # short -> integer
    field_unsigned_short: Annotated[int, 'H']  # unsigned short -> integer
    field_int: Annotated[int, 'i']  # int -> integer
    field_unsigned_int: Annotated[int, 'I']  # unsigned int -> integer
    field_long: Annotated[int, 'l']  # long -> integer
    field_unsigned_long: Annotated[int, 'L']  # unsigned long -> integer
    field_long_long: Annotated[int, 'q']  # long long -> integer
    field_unsigned_long_long: Annotated[int, 'Q']  # unsigned long long -> integer
    # Not allowed # field_ssize_t: Annotated[int, 'n']  # ssize_t -> integer
    # Not allowed # field_size_t: Annotated[int, 'N']  # size_t -> integer
    field_float_2: Annotated[float, 'e']  # (6) -> float
    field_float_4: Annotated[float, 'f']  # float -> float
    field_double: Annotated[float, 'd']  # double -> float
    field_char_array: Annotated[bytes, 's', 7]  # char[] -> bytes
    # TODO: field_char_array_p: Annotated[bytes, 'p', 7]  # char[] -> bytes
    # Not allowed field_void_pointer: Annotated[int, 'P']  # void* -> integer


CLASS_WITH_FORMATS_EXPECTED_TYPE_HINTS: Final = {
    'field_pad_byte': Annotated[None, 'x'],
    'field_char': Annotated[bytes, 'c'],
    'field_signed_char': Annotated[int, 'b'],
    'field_unsigned_char': Annotated[int, 'B'],
    'field_bool': Annotated[bool, '?'],
    'field_short': Annotated[int, 'h'],
    'field_unsigned_short': Annotated[int, 'H'],
    'field_int': Annotated[int, 'i'],
    'field_unsigned_int': Annotated[int, 'I'],
    'field_long': Annotated[int, 'l'],
    'field_unsigned_long': Annotated[int, 'L'],
    'field_long_long': Annotated[int, 'q'],
    'field_unsigned_long_long': Annotated[int, 'Q'],
    # Not allowed 'field_ssize_t': Annotated[int, 'n'],
    # Not allowed 'field_size_t': Annotated[int, 'N'],
    'field_float_2': Annotated[float, 'e'],
    'field_float_4': Annotated[float, 'f'],
    'field_double': Annotated[float, 'd'],
    'field_char_array': Annotated[bytes, 's', 7],
    # TODO: 'field_char_array_p': Annotated[bytes, 'p', 7],
    # Not allowed 'field_void_pointer': Annotated[int, 'P']
}

CLASS_WITH_FORMATS_EXPECTED_VALUES: Final = {
    'field_pad_byte': None,
    'field_char': b'\0',
    'field_signed_char': 0,
    'field_unsigned_char': 0,
    'field_bool': False,
    'field_short': 0,
    'field_unsigned_short': 0,
    'field_int': 0,
    'field_unsigned_int': 0,
    'field_long': 0,
    'field_unsigned_long': 0,
    'field_long_long': 0,
    'field_unsigned_long_long': 0,
    # Not allowed 'field_ssize_t': 0,
    # Not allowed 'field_size_t': 0,
    'field_float_2': 0,
    'field_float_4': 0,
    'field_double': 0,
    'field_char_array': b'\0\0\0\0\0\0\0',
    # TODO: 'field_char_array_p': b'\0',
    # Not allowed 'field_void_pointer': 0
}

CLASS_WITH_FORMATS_EXPECTED_VALUES_AS_TUPLE: Final = tuple(
    CLASS_WITH_FORMATS_EXPECTED_VALUES.values()  # here None for 'x' is also included
)


class TestClassWithFormats(unittest.TestCase):
    """ Test serialization/deserialization of class with all kinds formats,
        based on ClassWithFormats """
    def test_fields_are_extracted_in_order_and_right_content(self):
        actual_type_hints = get_type_hints(ClassWithFormats, include_extras=True)
        self.assertEqual(
            actual_type_hints,
            CLASS_WITH_FORMATS_EXPECTED_TYPE_HINTS
        )

    def test_all_fields_are_initialized(self):
        all_fields = ClassWithFormats()

        # All values shall be present
        for field_name, field_value in CLASS_WITH_FORMATS_EXPECTED_VALUES.items():
            self.assertTrue(hasattr(all_fields, field_name))
            self.assertEqual(getattr(all_fields, field_name), field_value)

        at = astuple(cast(Any, all_fields))  # here None for 'x' is also included
        self.assertEqual(
            at,
            CLASS_WITH_FORMATS_EXPECTED_VALUES_AS_TUPLE
        )

    def test_format_is_correct(self):
        self.assertEqual(
            '<xcbB?hHiIlLqQefd7s',
            cast(Any, ClassWithFormats).SERIALIZATION_FORMAT
        )

    def test_serialization(self):
        all_fields = ClassWithFormats()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        self.assertEqual(
            serialized,
            b'\0'  # padding
            b'\0'  # field_char
            b'\0'  # field_signed_char
            b'\0'  # field_unsigned_char
            b'\0'  # field_bool
            b'\0\0'  # field_short
            b'\0\0'  # field_unsigned_short
            b'\0\0\0\0'  # field_int
            b'\0\0\0\0'  # field_unsigned_int
            b'\0\0\0\0'  # field_long
            b'\0\0\0\0'  # field_unsigned_long
            b'\0\0\0\0\0\0\0\0'  # field_long_long
            b'\0\0\0\0\0\0\0\0'  # field_unsigned_long_long
            b'\0\0'  # field_float_2
            b'\0\0\0\0'  # field_float_4
            b'\0\0\0\0\0\0\0\0'  # field_double
            b'\0\0\0\0\0\0\0'  # field_char_array
        )

    def test_deserialization(self):
        all_fields = ClassWithFormats()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        deserialized = ClassWithFormats()
        cast(Any, deserialized).fill_in_from_bytes(serialized)

        # All values shall be present
        for field_name, field_value in CLASS_WITH_FORMATS_EXPECTED_VALUES.items():
            print(f"test_deserialization field {field_name} value {field_value}")
            self.assertTrue(hasattr(deserialized, field_name))
            deserialized_value = getattr(deserialized, field_name)
            self.assertEqual(
                deserialized_value, field_value,
                msg=f"field {field_name} value {deserialized_value} != {field_value}"
            )

        at = astuple(cast(Any, deserialized))
        self.assertEqual(
            at,
            CLASS_WITH_FORMATS_EXPECTED_VALUES_AS_TUPLE
        )


@serializable
class ClassWithFormatsAsArrays:
    """ To test all kinds of formats for serialization/deserialization """
    field_pad_byte: Annotated[None, 'x', 7]
    field_char: Annotated[list[bytes], 'c', 7]
    field_signed_char: Annotated[list[int], 'b', 7]
    field_unsigned_char: Annotated[list[int], 'B', 7]
    field_bool: Annotated[list[bool], '?', 7]
    field_short: Annotated[list[int], 'h', 7]
    field_unsigned_short: Annotated[list[int], 'H', 7]
    field_int: Annotated[list[int], 'i', 7]
    field_unsigned_int: Annotated[list[int], 'I', 7]
    field_long: Annotated[list[int], 'l', 7]
    field_unsigned_long: Annotated[list[int], 'L', 7]
    field_long_long: Annotated[list[int], 'q', 7]
    field_unsigned_long_long: Annotated[list[int], 'Q', 7]
    # Not allowed field_ssize_t: Annotated[list[int], 'n', 7]
    # Not allowed field_size_t: Annotated[list[int], 'N', 7]
    field_float_2: Annotated[list[float], 'e', 7]
    field_float_4: Annotated[list[float], 'f', 7]
    field_double: Annotated[list[float], 'd', 7]
    # That was already tested field_char_array: Annotated[bytes, 's', 7] = [b'\0\0\0\0\0\0\0'] * 7


CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_TYPE_HINTS: Final = {
    'field_pad_byte': Annotated[None, 'x', 7],
    'field_char': Annotated[list[bytes], 'c', 7],
    'field_signed_char': Annotated[list[int], 'b', 7],
    'field_unsigned_char': Annotated[list[int], 'B', 7],
    'field_bool': Annotated[list[bool], '?', 7],
    'field_short': Annotated[list[int], 'h', 7],
    'field_unsigned_short': Annotated[list[int], 'H', 7],
    'field_int': Annotated[list[int], 'i', 7],
    'field_unsigned_int': Annotated[list[int], 'I', 7],
    'field_long': Annotated[list[int], 'l', 7],
    'field_unsigned_long': Annotated[list[int], 'L', 7],
    'field_long_long': Annotated[list[int], 'q', 7],
    'field_unsigned_long_long': Annotated[list[int], 'Q', 7],
    # Not allowed 'field_ssize_t': Annotated[list[int], 'n', 7],
    # Not allowed 'field_size_t': Annotated[list[int], 'N', 7],
    'field_float_2': Annotated[list[float], 'e', 7],
    'field_float_4': Annotated[list[float], 'f', 7],
    'field_double': Annotated[list[float], 'd', 7],
    # That was already tested 'field_char_array': Annotated[bytes, 's', 7]
}


CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_VALUES: Final = {
    'field_pad_byte': None,
    'field_char': [b'\0'] * 7,
    'field_signed_char': [0] * 7,
    'field_unsigned_char': [0] * 7,
    'field_bool': [False] * 7,
    'field_short': [0] * 7,
    'field_unsigned_short': [0] * 7,
    'field_int': [0] * 7,
    'field_unsigned_int': [0] * 7,
    'field_long': [0] * 7,
    'field_unsigned_long': [0] * 7,
    'field_long_long': [0] * 7,
    'field_unsigned_long_long': [0] * 7,
    # Not allowed 'field_ssize_t': [0] * 7,
    # Not allowed 'field_size_t': [0] * 7,
    'field_float_2': [0] * 7,
    'field_float_4': [0] * 7,
    'field_double': [0] * 7,
    # That was already tested 'field_char_array': [b'\0\0\0\0\0\0\0'] * 7
}

CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_VALUES_AS_TUPLE: Final = tuple(
    CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_VALUES.values()
)


class TestClassWithFormatsAsArrays(unittest.TestCase):
    """ Test serialization/deserialization of class with all kinds formats,
        based on ClassWithFormatsAsArrays """
    def test_fields_are_extracted_in_order_and_right_content(self):
        actual_type_hints = get_type_hints(ClassWithFormatsAsArrays, include_extras=True)
        self.assertEqual(
            actual_type_hints,
            CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_TYPE_HINTS
        )

    def test_all_fields_are_initialized(self):
        all_fields = ClassWithFormatsAsArrays()

        # All values shall be present
        for field_name, field_value in CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_VALUES.items():
            self.assertTrue(hasattr(all_fields, field_name))
            self.assertEqual(getattr(all_fields, field_name), field_value)

        at = astuple(cast(Any, all_fields))  # here None for 'x' is also included
        self.assertEqual(
            at,
            CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_VALUES_AS_TUPLE
        )

    def test_format_is_correct(self):
        self.assertEqual(
            '<7x7c7b7B7?7h7H7i7I7l7L7q7Q7e7f7d',
            cast(Any, ClassWithFormatsAsArrays).SERIALIZATION_FORMAT
        )

    def test_serialization(self):
        all_fields = ClassWithFormatsAsArrays()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        self.assertEqual(
            serialized,
            b'\0' * 7 +  # padding
            b'\0' * 7 +  # field_char
            b'\0' * 7 +  # field_signed_char
            b'\0' * 7 +  # field_unsigned_char
            b'\0' * 7 +  # field_bool
            b'\0' * 14 +  # field_short
            b'\0' * 14 +  # field_unsigned_short
            b'\0' * 28 +  # field_int
            b'\0' * 28 +  # field_unsigned_int
            b'\0' * 28 +  # field_long
            b'\0' * 28 +  # field_unsigned_long
            b'\0' * 56 +  # field_long_long
            b'\0' * 56 +  # field_unsigned_long_long
            b'\0' * 14 +  # field_float_2
            b'\0' * 28 +  # field_float_4
            b'\0' * 56    # field_double
            # b'\0\0\0\0\0\0\0' * 7  # field_char_array
        )

    def test_deserialization(self):
        all_fields = ClassWithFormatsAsArrays()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        deserialized = ClassWithFormatsAsArrays()
        cast(Any, deserialized).fill_in_from_bytes(serialized)

        # All values shall be present
        for field_name, field_value in CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_VALUES.items():
            self.assertTrue(hasattr(deserialized, field_name))
            deserialized_value = getattr(deserialized, field_name)
            self.assertEqual(
                deserialized_value, field_value,
                msg=f"field {field_name} value {deserialized_value} != {field_value}"
            )

        at = astuple(cast(Any, deserialized))
        self.assertEqual(
            at,
            CLASS_WITH_FORMATS_AS_ARRAYS_EXPECTED_VALUES_AS_TUPLE
        )


# NOTE: the same as above but now C/C++ types instead of formats
#       all types used below correspond to keys from CPP_TO FORMAT
@serializable
class ClassWithTypes:
    """ To test all kinds of formats for serialization/deserialization """
    field_pad_byte: Annotated[None, 'uint8_t']

    field_char: Annotated[bytes, 'char']  # char -> bytes of length 1
    field_signed_char: Annotated[int, 'int8_t']
    field_unsigned_char: Annotated[int, 'uint8_t']
    field_bool: Annotated[bool, 'bool']
    field_short: Annotated[int, 'int16_t']
    field_unsigned_short: Annotated[int, 'uint16_t']
    field_int: Annotated[int, 'int32_t']
    field_unsigned_int: Annotated[int, 'uint32_t']
    # matches above (is the same) field_long: Annotated[int, 'int32_t']
    # matches above (is the same) field_unsigned_long: Annotated[int, 'uint32_t']
    field_long_long: Annotated[int, 'int64_t']
    field_unsigned_long_long: Annotated[int, 'uint64_t']
    # Not allowed # field_ssize_t: Annotated[int, 'ssize_t']  # ssize_t -> integer
    # Not allowed # field_size_t: Annotated[int, 'size_t']  # size_t -> integer
    # TODO: later field_float_2: Annotated[float, 'uint16_t']
    field_float_4: Annotated[float, 'float']
    field_double: Annotated[float, 'double']
    field_char_array: Annotated[bytes, 'char', 7]
    

CLASS_WITH_TYPES_EXPECTED_TYPE_HINTS: Final = {
    'field_pad_byte': Annotated[None, 'uint8_t'],
    'field_char': Annotated[bytes, 'char'],
    'field_signed_char': Annotated[int, 'int8_t'],
    'field_unsigned_char': Annotated[int, 'uint8_t'],
    'field_bool': Annotated[bool, 'bool'],
    'field_short': Annotated[int, 'int16_t'],
    'field_unsigned_short': Annotated[int, 'uint16_t'],
    'field_int': Annotated[int, 'int32_t'],
    'field_unsigned_int': Annotated[int, 'uint32_t'],
    # matches above (is the same) 'field_long': Annotated[int, 'int32_t'],
    # matches above (is the same) 'field_unsigned_long': Annotated[int, 'uint32_t'],
    'field_long_long': Annotated[int, 'int64_t'],
    'field_unsigned_long_long': Annotated[int, 'uint64_t'],
    # Not allowed 'field_ssize_t': Annotated[int, 'ssize_t'],
    # Not allowed 'field_size_t': Annotated[int, 'size_t'],
    # TODO: later 'field_float_2': Annotated[float, 'uint16_t'],
    'field_float_4': Annotated[float, 'float'],
    'field_double': Annotated[float, 'double'],
    'field_char_array': Annotated[bytes, 'char', 7]
}

CLASS_WITH_TYPES_EXPECTED_VALUES: Final = {
    'field_pad_byte': None,
    'field_char': b'\0',
    'field_signed_char': 0,
    'field_unsigned_char': 0,
    'field_bool': False,
    'field_short': 0,
    'field_unsigned_short': 0,
    'field_int': 0,
    'field_unsigned_int': 0,
    # matches above (is the same declaration) 'field_long': 0,
    # matches above (is the same declaration) 'field_unsigned_long': 0,
    'field_long_long': 0,
    'field_unsigned_long_long': 0,
    # Not allowed 'field_ssize_t': 0,
    # Not allowed 'field_size_t': 0,
    # TODO: later 'field_float_2': 0,
    'field_float_4': 0,
    'field_double': 0,
    'field_char_array': b'\0\0\0\0\0\0\0'
}

CLASS_WITH_TYPES_EXPECTED_VALUES_AS_TUPLE: Final = tuple(
    CLASS_WITH_TYPES_EXPECTED_VALUES.values()  # here None for 'x' is also included
)


class TestClassWithTypes(unittest.TestCase):
    """ Test serialization/deserialization of class with all kinds formats,
        based on ClassWithTypes """
    def test_fields_are_extracted_in_order_and_right_content(self):
        actual_type_hints = get_type_hints(ClassWithTypes, include_extras=True)
        self.assertEqual(
            actual_type_hints,
            CLASS_WITH_TYPES_EXPECTED_TYPE_HINTS
        )

    def test_all_fields_are_initialized(self):
        all_fields = ClassWithTypes()

        # All values shall be present
        for field_name, field_value in CLASS_WITH_TYPES_EXPECTED_VALUES.items():
            self.assertTrue(hasattr(all_fields, field_name))
            self.assertEqual(getattr(all_fields, field_name), field_value)

        at = astuple(cast(Any, all_fields))  # here None for 'x' is also included
        self.assertEqual(
            at,
            CLASS_WITH_TYPES_EXPECTED_VALUES_AS_TUPLE
        )

    def test_format_is_correct(self):
        self.assertEqual(
            '<xcbB?hHiIqQfd7s',  # without e here
            cast(Any, ClassWithTypes).SERIALIZATION_FORMAT
        )

    def test_serialization(self):
        all_fields = ClassWithTypes()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        self.assertEqual(
            serialized,
            b'\0'  # padding
            b'\0'  # field_char
            b'\0'  # field_signed_char
            b'\0'  # field_unsigned_char
            b'\0'  # field_bool
            b'\0\0'  # field_short
            b'\0\0'  # field_unsigned_short
            b'\0\0\0\0'  # field_int
            b'\0\0\0\0'  # field_unsigned_int
            # matches above (is the same declaration) b'\0\0\0\0'  # field_long
            # matches above (is the same declaration) b'\0\0\0\0'  # field_unsigned_long
            b'\0\0\0\0\0\0\0\0'  # field_long_long
            b'\0\0\0\0\0\0\0\0'  # field_unsigned_long_long
            # TODO: later  b'\0\0'  # field_float_2
            b'\0\0\0\0'  # field_float_4
            b'\0\0\0\0\0\0\0\0'  # field_double
            b'\0\0\0\0\0\0\0'  # field_char_array
        )


    def test_deserialization(self):
        all_fields = ClassWithTypes()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        deserialized = ClassWithTypes()
        cast(Any, deserialized).fill_in_from_bytes(serialized)

        # All values shall be present
        for field_name, field_value in CLASS_WITH_TYPES_EXPECTED_VALUES.items():
            self.assertTrue(hasattr(deserialized, field_name))
            deserialized_value = getattr(deserialized, field_name)
            self.assertEqual(
                deserialized_value, field_value,
                msg=f"field {field_name} value {deserialized_value} != {field_value}"
            )

        at = astuple(cast(Any, deserialized))
        self.assertEqual(
            at,
            CLASS_WITH_TYPES_EXPECTED_VALUES_AS_TUPLE
        )


@serializable
class ClassWithTypesAsArrays:
    """ To test all kinds of formats for serialization/deserialization """
    field_pad_byte: Annotated[None, 'uint8_t', 7]
    field_char: Annotated[list[bytes], 'char', 7]
    field_signed_char: Annotated[list[int], 'int8_t', 7]
    field_unsigned_char: Annotated[list[int], 'uint8_t', 7]
    field_bool: Annotated[list[bool], 'bool', 7]
    field_short: Annotated[list[int], 'int16_t', 7]
    field_unsigned_short: Annotated[list[int], 'uint16_t', 7]
    field_int: Annotated[list[int], 'int32_t', 7]
    field_unsigned_int: Annotated[list[int], 'uint32_t', 7]
    # matches above (is the same) field_long: Annotated[list[int], 'int32_t', 7]
    # matches above (is the same) field_unsigned_long: Annotated[list[int], 'uint32_t', 7]
    field_long_long: Annotated[list[int], 'int64_t', 7]
    field_unsigned_long_long: Annotated[list[int], 'uint64_t', 7]
    # Not allowed field_ssize_t: Annotated[list[int], 'ssize_t', 7]
    # Not allowed field_size_t: Annotated[list[int], 'size_t', 7]
    # TODO: later field_float_2: Annotated[float, 'uint16_t', 7]
    field_float_4: Annotated[list[float], 'float', 7]
    field_double: Annotated[list[float], 'double', 7]
    # That was already tested field_char_array: Annotated[bytes, 'char', 7] = [b'\0\0\0\0\0\0\0'] * 7


CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_TYPE_HINTS: Final = {
    'field_pad_byte': Annotated[None, 'uint8_t', 7],
    'field_char': Annotated[list[bytes], 'char', 7],
    'field_signed_char': Annotated[list[int], 'int8_t', 7],
    'field_unsigned_char': Annotated[list[int], 'uint8_t', 7],
    'field_bool': Annotated[list[bool], 'bool', 7],
    'field_short': Annotated[list[int], 'int16_t', 7],
    'field_unsigned_short': Annotated[list[int], 'uint16_t', 7],
    'field_int': Annotated[list[int], 'int32_t', 7],
    'field_unsigned_int': Annotated[list[int], 'uint32_t', 7],
    # matches above (is the same) 'field_long': Annotated[list[int], 'int32_t', 7],
    # matches above (is the same) 'field_unsigned_long': Annotated[list[int], 'uint32_t', 7],
    'field_long_long': Annotated[list[int], 'int64_t', 7],
    'field_unsigned_long_long': Annotated[list[int], 'uint64_t', 7],
    # Not allowed 'field_ssize_t': Annotated[list[int], 'ssize_t', 7],
    # Not allowed 'field_size_t': Annotated[list[int], 'size_t', 7],
    # TODO: later field_float_2: Annotated[float, 'uint16_t', 7],
    'field_float_4': Annotated[list[float], 'float', 7],
    'field_double': Annotated[list[float], 'double', 7],
    # That was already tested 'field_char_array': Annotated[bytes, 'char', 7]
}


CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_VALUES: Final = {
    'field_pad_byte': None,
    'field_char': [b'\0'] * 7,
    'field_signed_char': [0] * 7,
    'field_unsigned_char': [0] * 7,
    'field_bool': [False] * 7,
    'field_short': [0] * 7,
    'field_unsigned_short': [0] * 7,
    'field_int': [0] * 7,
    'field_unsigned_int': [0] * 7,
    # matches above (is the same) 'field_long': [0] * 7,
    # matches above (is the same) 'field_unsigned_long': [0] * 7,
    'field_long_long': [0] * 7,
    'field_unsigned_long_long': [0] * 7,
    # Not allowed 'field_ssize_t': [0] * 7,
    # Not allowed 'field_size_t': [0] * 7,
    # TODO: later 'field_float_2': [0] * 7,
    'field_float_4': [0] * 7,
    'field_double': [0] * 7,
    # That was already tested 'field_char_array': [b'\0\0\0\0\0\0\0'] * 7
}

CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_VALUES_AS_TUPLE: Final = tuple(
    CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_VALUES.values()
)


class TestClassWithTypesAsArrays(unittest.TestCase):
    """ Test serialization/deserialization of class with all kinds formats,
        based on ClassWithTypesAsArrays """
    def test_fields_are_extracted_in_order_and_right_content(self):
        actual_type_hints = get_type_hints(ClassWithTypesAsArrays, include_extras=True)
        self.assertEqual(
            actual_type_hints,
            CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_TYPE_HINTS
        )

    def test_all_fields_are_initialized(self):
        all_fields = ClassWithTypesAsArrays()

        # All values shall be present
        for field_name, field_value in CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_VALUES.items():
            self.assertTrue(hasattr(all_fields, field_name))
            self.assertEqual(getattr(all_fields, field_name), field_value)

        at = astuple(cast(Any, all_fields))  # here None for 'x' is also included
        self.assertEqual(
            at,
            CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_VALUES_AS_TUPLE
        )

    def test_format_is_correct(self):
        self.assertEqual(
            '<7x7c7b7B7?7h7H7i7I7q7Q7f7d',
            cast(Any, ClassWithTypesAsArrays).SERIALIZATION_FORMAT
        )

    def test_serialization(self):
        all_fields = ClassWithTypesAsArrays()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        self.assertEqual(
            serialized,
            b'\0' * 7 +  # padding
            b'\0' * 7 +  # field_char
            b'\0' * 7 +  # field_signed_char
            b'\0' * 7 +  # field_unsigned_char
            b'\0' * 7 +  # field_bool
            b'\0' * 14 +  # field_short
            b'\0' * 14 +  # field_unsigned_short
            b'\0' * 28 +  # field_int
            b'\0' * 28 +  # field_unsigned_int
            # matches above (is the same) b'\0' * 28 +  # field_long
            # matches above (is the same) b'\0' * 28 +  # field_unsigned_long
            b'\0' * 56 +  # field_long_long
            b'\0' * 56 +  # field_unsigned_long_long
            # Not allowed b'\0' * 28 +  # field_ssize_t
            # Not allowed b'\0' * 28 +  # field_size_t
            # TODO: later b'\0' * 14 +  # field_float_2
            b'\0' * 28 +  # field_float_4
            b'\0' * 56    # field_double
            # b'\0\0\0\0\0\0\0' * 7  # field_char_array
        )

    def test_deserialization(self):
        all_fields = ClassWithTypesAsArrays()
        serialized = cast(Any, all_fields).serialize_to_bytes()
        deserialized = ClassWithTypesAsArrays()
        cast(Any, deserialized).fill_in_from_bytes(serialized)

        # All values shall be present
        for field_name, field_value in CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_VALUES.items():
            self.assertTrue(hasattr(deserialized, field_name))
            deserialized_value = getattr(deserialized, field_name)
            self.assertEqual(
                deserialized_value, field_value,
                msg=f"field {field_name} value {deserialized_value} != {field_value}"
            )

        at = astuple(cast(Any, deserialized))
        self.assertEqual(
            at,
            CLASS_WITH_TYPES_AS_ARRAYS_EXPECTED_VALUES_AS_TUPLE
        )

# Tests for serialization/deserialization of class with nested classes


@serializable
class NestedClass:
    """ To test serialization/deserialization of nested classes """
    field_int: Annotated[int, 'int32_t']
    field_char: Annotated[bytes, 'char']
    field_float: Annotated[float, 'float']


@serializable
class ClassWithNested:
    """ To test serialization/deserialization of nested classes """
    field_nested: NestedClass
    field_int: Annotated[int, 'int32_t']
    field_char: Annotated[bytes, 'char']
    field_nested_array: Annotated[list[NestedClass], 5]


