# Pentago

[![Build Status](https://img.shields.io/github/workflow/status/evanfpearson/pentago/Continuous%20Integration)](https://github.com/evanfpearson/pentago/actions?query=workflow%3A%22Continuous+Integration%22)

Terminal interface for the board game Pentago. Written in Python.

## Requirements
  - Python3
  - Make

## Install Instructions

  - Clone this repository
  - Change directory to the root directory of this repo
  - Download python requirements: ```pip install -r requirements.txt```
  - Run Game: ```make run```

## Game instructions

Pentago is two-player strategy board game which is played on a 6x6 board divided into four 3x3 quadrants.

Taking turns, both players place a marble onto an empty space on the board, and then rotate one of the quadrants by 90 degress either clockwise or anti-clockwise. Any of the players win if they get five of their marbles in a vertical, horizontal or diagonal row (before or after the rotation step).

## CLI instructions

  - Use the arrow keys to select marble placement / block to rotate.
  - Use enter key to confirm marble placement
  - Use the ```[``` - anticlockwise, and ```]``` - clockwise keys to select rotation direction
