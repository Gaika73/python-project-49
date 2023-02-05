#!/usr/bin/env python3
import brain_games.cli
import brain_games.brain_gcd


def main():
    name = brain_games.cli.welcome_user()
    brain_games.brain_gcd.start(name)
