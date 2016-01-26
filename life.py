# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 08:04:02 2016

@author: Tom

http://glowingpython.blogspot.com/2015/10/game-of-life-with-python.html
http://rosettacode.org/wiki/Conway%27s_Game_of_Life

"""

import numpy as np
import matplotlib.pyplot as plt


def life(X, steps):
    """
     Conway's Game of Life.
     - X, matrix with the initial state of the game.
     - steps, number of generations.
    """
    def roll_it(x, y):
        # rolls the matrix X in a given direction
        # x=1, y=0 on the left;  x=-1, y=0 right;
        # x=0, y=1 top; x=0, y=-1 down; x=1, y=1 top left; ...
        return np.roll(np.roll(X, y, axis=0), x, axis=1)

    for _ in range(steps):
        # count the number of neighbours
        # the universe is considered toroidal
        Y = roll_it(-1, -1) + roll_it(-1, 0) + roll_it(-1, 1) \
            + roll_it(0, -1) + roll_it(0, 1) \
            + roll_it(1, -1) + roll_it(1, 0) + roll_it(1, 1)

        # game of life rules
        X = np.logical_or(np.logical_and(X, Y == 2), Y == 3)
        X = X.astype(np.int8)
        yield X


def init():
    X = np.zeros((10, 10), dtype=np.int8)

    # Blinker
    # X[2, 1:4] = 1

    # R-pentomino
    # X[3, 2:4] = 1
    # X[4, 1:3] = 1
    # X[5, 2] = 1

    # Glider
    X[1, 2] = 1
    X[2, 3] = 1
    X[3, 1:4] = 1

    return X


def display(generation, X):
    print('Generation: ', generation)
    m, n = X.shape
    for i in range(m):
        s = ''
        for j in range(n):
            if X[i, j]:
                s += ' #'
            else:
                s += ' .'
        print(s)
    print('\n')


def main():
    X = init()

    generation = 0
    display(generation, X)
    generation += 1

    # fig = plt.figure()
    # fig.patch.set_facecolor('black')
    # plt.spy(X)
    # plt.show()
    # print('\n', X)

    for x in life(X, 40):
        display(generation, x)
        generation += 1

        # plt.clf()
        # plt.spy(x)
        # plt.show()
        # print('\n', x)


if __name__ == '__main__':
    main()
