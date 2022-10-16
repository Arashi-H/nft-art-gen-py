""" Retroactively replaces the JSON Image 'BaseURI' file after it is known """

import json

from parse_yaml import read_yaml


def update_base_uri(config_file: object) -> None:
    """Takes an input of the metadata URI and amount of json files and updates
    all of the json files with the new URI. This is necessary for places like IPFS
    as you cannot get the URI until the images have been uploaded."""

    amount = config_file['amount']
    uri_prefix = config_file['uri_prefix']
    new_uri = config_file['new_uri']

    if config_file['id_from_one']:
        edition = 1
    else:
        edition = 0

    for _ in range(amount):

        json_path = f'build/json/{edition}.json'

        # TODO: These probably don't need to be two file operations separately
        # Opens json file
        with open(json_path, 'r', encoding='utf-8') as infile:

            # Load the opened json file into a Python dict
            data = json.load(infile)

            # Changes the necessary data in the now Python dictionary
            data['image'] = f'{uri_prefix}{new_uri}/{edition}.png'

        # Opens the original json file and writes the new data
        with open(json_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)

        edition += 1

    print('Base URIs Updated')


read_config = read_yaml()
update_base_uri(read_config)
