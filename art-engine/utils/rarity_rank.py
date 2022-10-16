import json


def calculate_mean(amount: int, edition: int) -> dict:
    harmonic_means = dict()

    for _ in range(amount):

        json_path = f'build/json/{edition}.json'

        with open(json_path, 'r', encoding='utf-8') as infile:

            data = json.load(infile)
            token_attributes = data['attributes']

            total_traits = len(token_attributes)
            rarity_sum = 0

            for attr in token_attributes:
                rarity_sum += (1 / attr['count'])

            mean = total_traits / rarity_sum
            rounded_mean = round(mean, 3)

            harmonic_means[edition] = f'{rounded_mean}%'

        data['rarity'] = dict()
        data['rarity']['harmonic'] = dict()
        data['rarity']['harmonic']['score'] = f'{rounded_mean}%'

        # Opens the original json file and writes the new data
        with open(json_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)

        edition += 1

    return harmonic_means


def add_rarity_rank(harmonic_means: dict) -> None:
    sorted_tokens = sorted(harmonic_means.items(), key=lambda x: x[1])

    rank = 1
    for token in sorted_tokens:

        json_path = f'build/json/{token[0]}.json'

        with open(json_path, 'r', encoding='utf-8') as infile:

            data = json.load(infile)
            data['rarity']['harmonic']['rank'] = rank

        with open(json_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)

        rank += 1
