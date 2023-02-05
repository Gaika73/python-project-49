#!/usr/bin/progression python3
import brain_games.cli
import brain_games.brain_progression


def main():
    name = brain_games.cli.welcome_user()
    brain_games.brain_progression.start(name)
