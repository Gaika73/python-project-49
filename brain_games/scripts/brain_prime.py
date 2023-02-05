#!/usr/bin/prime python3
import brain_games.cli
import brain_games.brain_prime


def main():
    name = brain_games.cli.welcome_user()
    brain_games.brain_prime.start(name)
