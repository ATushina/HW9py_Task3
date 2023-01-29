from model import run_action
from view import select_action


def run_prog():
     action = select_action()
     run_action(action)