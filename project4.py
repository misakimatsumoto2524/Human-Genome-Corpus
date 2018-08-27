import os
import codecs
from itertools import islice

def target_list():
    target = []
    with open("targets", encoding='utf-8') as f:
        while True:
            next_n_lines = list(islice(f, 1000))
            target += next_n_lines
            if not next_n_lines:
                break
    target = list(map(lambda s: s.strip(), target))
    print(target)


target_list()
