""" Adds a trait count and frequency % to the metadata of each token. """

import json

def create_counts(edition: int, amount: int) -> dict:
    """ Loops through all of the json metadata files, creates a frequency tabble
    with counts of all trait values, and returns it.
    """
    attributes_count = dict()

    for _ in range(amount):

        json_path = f'build/json/{edition}.json'

        with open(json_path, 'r', encoding='utf-8') as infile:

            data = json.load(infile)
            token_attributes = data['attributes']

            for attr in token_attributes:
                attr_key = (attr['trait_type'], attr['value'])
                if attr_key not in attributes_count:
                    attributes_count[attr_key] = 1
                else:
                    attributes_count[attr_key] += 1

        edition += 1

    return attributes_count



def calculate_percentages(amount: int, attributes_count: dict) -> dict:
    """ Based on the calculated counts, creates a frequency table this time with the 
    percentage a trait occurs - rounded to three decimal places. 
    """
    attribute_percentages = dict()

    # lambda func to calculate percentage
    def percent(count): return (count / amount) * 100

    for attribute in attributes_count:
        freq_percent = percent(attributes_count[attribute])
        freq_percent = round(freq_percent, 3)

        attribute_percentages[attribute] = f'{freq_percent}%'

    return attribute_percentages


def update_metadata(edition: int, amount: int, attribute_count: dict, attribute_freq: dict) -> None:
    """ Reads in the calculated count and frequency, loops through each token, and adds
    count and value to their respective trait values.
    """

    for _ in range(amount):

        json_path = f'build/json/{edition}.json'

        with open(json_path, 'r', encoding='utf-8') as infile:

            data = json.load(infile)
            token_attributes = data['attributes']

            for attr in token_attributes:
                attr_key = (attr['trait_type'], attr['value'])

                count = attribute_count[attr_key]
                freq = attribute_freq[attr_key]

                attr['count'] = count
                attr['frequency'] = freq

        data['attributes'] = token_attributes

        with open(json_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)

        edition += 1
