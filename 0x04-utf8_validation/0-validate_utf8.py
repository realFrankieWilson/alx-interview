#!/usr/bin/python3


def validUTF8(data):
    """
    A method that determinse if a given data set represents
    a valid UTF-8 encoding.
    Arg:
        data (List(Int)): List of integers to be processed.
    """

    # Number of bytes in the current UTF-* character
    n_bytes = 0

    # For each integer in the data array
    for n in data:
        # Get the binary representation(Only the least significant 8 bits)
        # for any givien number and discard the rest.
        bin_rep = format(n, "#010b")[-8:]

        # start processing only if this is the case.
        if n_bytes == 0:
            # Get the number of 1s in the beginning of the string.
            # This is the number of bytes that make up the current
            # UTF-8 character.
            for bit in bin_rep:
                if bit == "0":
                    break
                n_bytes += 1

            # 1 byte characters
            if n_bytes == 0:
                continue
        else:
            # Examine the current UTF-8 character.
            if not (bin_rep[0] == "1" and bin_rep[1] == "0"):
                return False

        # Reduce the number of bytes to process by 1 after each number.
        n_bytes -= 1

    return n_bytes == 0
