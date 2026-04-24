
OVERVIEW

The overall goal is to create a web based tic-tac-toe game as a learning experience for AWS development. The application
requires a complete search space of all game states. This project creates the game state data. Ultimately this data will
be stored in a DynamoDb table. It will also have a command line version of the game for testing purposes.

A further project will create a REST web service that serves game states and a React web page. It will also include the
necessary scripts to construct all the needed resources on AWS. The stack will be React, Waitress, EC2, Python 3, Flask,
Jinja and DynamoDB. The project is available from Github but not PyPl. It was written using Python 3.14.

In the future, projects could be developed to implement using lambdas or implement on Google Cloud or Microsoft Azure.
It could also be a jumping off point for training a neural network.

INCLUDED

    1. classes and function for creating the game state
    2. a class for working with game states in JSON
    3. functions to pickle the tree of game states
    4. unit tests
    5. a command line version of the game

SETUP & RUN

    dependencies: python 3, pytest

    setup:
        (for Windows, in a command window, from your python workspace)
        mkdir PyTicTacToe
        cd PyTicTacToe
        python -m venv .venv
        pip install pytest

    tests:
        .venv\Scripts\activate
        python darrought66\tic_tac_toe\pickle_game_states.py
        pytest tests\tests.py

    tests:
        .venv\Scripts\activate
        python darrought66\tic_tac_toe\console_app.py

CONTRIBUTING

I am not anticipating pull requests. Send me an email first explaining what your plan is.

It is Apache license, meaning your free to use it however you wish, whether that be an example in a course, book, Udemy
or YouTube video or start your own project doing it your way. Indeed, I would love to know if you found this useful.

CONTACTS

    T. "Rob" Darrough Jr.   RobDarrough0@gmail.com   https://www.darrought66.com

