import argparse
from importlib import import_module

LOCATION = 'commands.'

parser = argparse.ArgumentParser()

parser.add_argument('command', type=str)

args = parser.parse_args()
command = args.command.replace(':', '.')

try:
  process = import_module(f'{LOCATION}{command}')
  process.exec()
except Exception as inst:
  print(inst)
