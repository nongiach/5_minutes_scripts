#!/usr/bin/python3

import re
import clize
from faker import Faker

def main(filename, fake_file, link_file):
    fake = Faker()
    with open(filename) as F, open(fake_file, 'w') as Ffake, open(link_file, 'w') as Flink:
        for line in F:
            name = fake.name().lower().replace(' ', '.')
            Ffake.write(re.sub('^[^:]*:', f'{name}:', line))
            Flink.write(re.sub('^', f'{name}:', line))

if __name__ == "__main__":
    clize.run(main)
