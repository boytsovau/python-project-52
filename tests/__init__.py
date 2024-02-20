import os
import json

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'fixtures'
)


def load_fixture_data(filename):
    fixture_file_path = os.path.join(FIXTURE_DIR, filename)
    with open(fixture_file_path, 'r') as file:
        return json.load(file)
