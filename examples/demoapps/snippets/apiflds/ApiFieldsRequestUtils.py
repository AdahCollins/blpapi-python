from blpapi import Name

ID = Name("id")
FIELD_INFO = Name("fieldInfo")
MNEMONIC = Name("mnemonic")
DESCRIPTION = Name("description")
FIELD_ERROR = Name("fieldError")
MESSAGE = Name("message")

ID_LEN = 13
MNEMONIC_LEN = 36
DESC_LEN = 40
CAT_NAME_LEN = 40


def printHeader():
    print(
        f'{"FIELD ID".ljust(ID_LEN)}'
        f'{"MNEMONIC".ljust(MNEMONIC_LEN)}'
        f'{"DESCRIPTION".ljust(DESC_LEN)}'
    )
    print(
        f'{"-----------".ljust(ID_LEN)}'
        f'{"-----------".ljust(MNEMONIC_LEN)}'
        f'{"-----------".ljust(DESC_LEN)}'
    )


def printField(field):
    fieldId = field[ID]
    if FIELD_INFO in field:
        fieldInfo = field[FIELD_INFO]
        fieldMnemonic = fieldInfo[MNEMONIC]
        fieldDesc = fieldInfo[DESCRIPTION]

        print(
            f"{fieldId.ljust(ID_LEN)}"
            f"{fieldMnemonic.ljust(MNEMONIC_LEN)}"
            f"{fieldDesc.ljust(DESC_LEN)}"
        )
    else:
        errorMsg = field[FIELD_ERROR][MESSAGE]

        print()
        print(f" ERROR: {fieldId} - {errorMsg}")


__copyright__ = """
Copyright 2021, Bloomberg Finance L.P.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: The above copyright
notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""
