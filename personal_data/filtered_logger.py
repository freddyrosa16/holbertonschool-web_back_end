#!/usr/bin/env python3
"""
This module provides a function to obfuscate specific fields in a log message.

The `filter_datum` function takes a list of field names, a redaction string,
and a log message, and replaces the values of the specified fields with the
redaction string.
"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
   Obfuscates specified fields in a log message.

   Args:
       fields (list): List of field names to be obfuscated.
       redaction (str): The string to replace the field values with.
       message (str): The log message containing field-value pairs.
       separator (str): The character that separates fields in the message.

   Returns:
       str: The log message with obfuscated field values.
    """
    result = message
    for field in fields:
        construct = f"(?<={field}=)(.*?)(?={separator})"
        result = re.sub(construct, redaction, result)
    return result
