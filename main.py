import pyperclip
from LatLon23 import LatLon

import mgrs


def normalize_string(input_string):
    normalized_string = input_string
    while normalized_string.index('°') < 2:
        normalized_string = '0' + normalized_string
    if (normalized_string.rindex('′') - normalized_string.index('°')) == 2:
        normalized_string = normalized_string[:normalized_string.index('°') + 1] \
                            + '0' + normalized_string[normalized_string.index('′') - 1:]
    if (normalized_string.index('.') - normalized_string.index('′')) == 2:
        normalized_string = normalized_string[:normalized_string.index('′') + 1] \
                            + '0' + normalized_string[normalized_string.index('.') - 1:]
    return normalized_string


def add_after_every_n(iterator, item_to_add='\n', after_every=2):
    for i, element in enumerate(iterator, 1):
        yield element + item_to_add
        if i % after_every == 0:
            yield item_to_add


if __name__ == '__main__':
    try:
        clipboard_data = pyperclip.paste().splitlines()
        coord_list = []
        for line in clipboard_data:
            if len(line) == 0:
                continue
            elevation = ''
            mgrs_data = line.rstrip().split(' ')
            if len(mgrs_data) > 1:
                elevation = mgrs_data[1]
            position = mgrs.MGRStoLL(mgrs_data[0])
            ll_data = LatLon(float(position['lat']), float(position['lon']))
            ll_data_str = ll_data.to_string('d%°%m%′%S%%H')
            lat = ll_data_str[0][:ll_data_str[0].find('.') + 3] + ll_data_str[0][-1]
            lon = ll_data_str[1][:ll_data_str[1].find('.') + 3] + ll_data_str[1][-1]
            coord_list.append(f'{normalize_string(lat)} {normalize_string(lon)} {elevation}')
        clipboard_data = ''.join(add_after_every_n(coord_list))[:-2 if len(coord_list) % 2 == 0 else -1]
        pyperclip.copy(clipboard_data)
    except ValueError:
        print('ValueError, check the coordinates are correct.')
        input()
    except Exception as e:
        print(f'{e}')
        input()
