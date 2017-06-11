"""Rollingstock editor."""

import os
from contextlib import contextmanager

PRESETS_PATH = os.path.join(os.path.abspath('.'), 'presets')
RS_PASSENGER_FILENAME = 'tabor_pasazerski.txt'
RS_FREIGHT_FILENAME = 'tabor_towarowy.txt'


@contextmanager
def _open_file(filename):
    """Generic open file function handling edge cases."""
    full_path = os.path.join(PRESETS_PATH, filename)
    if os.path.exists(full_path):
        with open(full_path) as file_desc:
            print('File {} ...OK'.format(filename))
            yield file_desc
    else:
        print('Missing file {}'.format(filename))
    return


def load_file(filename):
    """Load and return file content."""
    with _open_file(filename) as file_desc:
        return file_desc.read() if file_desc is not None else ''


def get_list_from_file(filename):
    """Read and return file items split by semicolons."""
    entry_list = []
    with _open_file(filename) as file_desc:
        if file_desc is not None:
            for line in file_desc:
                entry_list.extend(line.rstrip().split(';'))
    return entry_list


def compare():
    """Compare results of extractick rollingstock data in two ways."""
    rs_content_freight = load_file(RS_FREIGHT_FILENAME)
    rs_content_passenger = load_file(RS_PASSENGER_FILENAME)

    print('File content test:\n{0} {1}'.format(
        rs_content_passenger,
        rs_content_freight,
    ))

    print()  # One enter space

    # Railroad rolling stock list
    rs_passenger_list = get_list_from_file(RS_PASSENGER_FILENAME)
    rs_freight_list = get_list_from_file(RS_FREIGHT_FILENAME)

    print('List content test:\n{0} {1}'.format(
        rs_passenger_list,
        rs_freight_list,
    ))

if __name__ == '__main__':
    compare()
