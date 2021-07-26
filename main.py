import telegram
import argparse
import subprocess
import yaml


def load_config(config_path):
    with open(config_path) as f:
        return yaml.load(f, Loader=yaml.Loader)


def send_message(message):
    BOT.send_message(text=message, chat_id=CONFIG['chat_id'])


CONFIG = load_config('config.yaml')
BOT = telegram.Bot(token=CONFIG['token'])


def main(args):

    p = subprocess.Popen([f"{args['interpreter']}", f"{args['program']}", f"{args['arguments']}"],
                         stdout=subprocess.PIPE)
    output, err = p.communicate()
    output = output.decode('utf-8')

    send_message(f"Done!\n Process output: {output}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Program for running programs with notifications in telegram')

    parser.add_argument('interpreter', help='path to interpreter which executes python program')
    parser.add_argument('program', help='path to program to execute')
    parser.add_argument('arguments', help='arguments to program, separated by space')

    args = parser.parse_args()
    args = vars(args)
    main(args)

