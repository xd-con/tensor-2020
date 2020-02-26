import yaml
import os
from os.path import join as pjoin

config_path = pjoin(os.path.dirname(__file__), '../site/config.yml')

data = yaml.safe_load(open(config_path, 'r'))

table_head = [
    '| Time  | Slot                      | Presenter    |',
    '| ----- | ------------------------- | ------------ |'
]

schedule = []

for day in data['params']['Schedule']:
    schedule += ['### ' + day['day'] + '\n']
    schedule.extend(table_head)

    for slot in day['slots']:
        field = lambda k: slot.get(k, '')
        line = f'| {field("time")} | {field("name")} | {field("presenter")} |'
        schedule.append(line)

    schedule += ['']

print('\n'.join(schedule), end='')
