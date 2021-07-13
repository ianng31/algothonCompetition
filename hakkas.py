#!/usr/bin/env python

# RENAME THIS FILE WITH YOUR TEAM NAME.

import numpy as np

nInst = 100
currentPos = np.zeros(nInst)

# Dummy algorithm to demonstrate function format.


def getAverage(instrument, prcSoFar):
    prices = prcSoFar[instrument]
    return np.average(prices[-150:])


def getTodaysPrice(instrument, prcSoFar):
    return prcSoFar[instrument, -1]


def getPreviousXDaysToSell(x, instrument, prcSoFar):
    return np.max(prcSoFar[instrument][-x:]) == getTodaysPrice(instrument, prcSoFar)


def getPreviousXDaysToBuy(x, instrument, prcSoFar):
    return np.min(prcSoFar[instrument][-x:]) == getTodaysPrice(instrument, prcSoFar)


def strategy(instrument, prcSoFar, days):
    if getTodaysPrice(instrument, prcSoFar) > getAverage(instrument, prcSoFar):
        if getPreviousXDaysToSell(days, instrument, prcSoFar):
            return -300
    else:
        if getPreviousXDaysToBuy(days, instrument, prcSoFar):
            return 300

    return 0


def getMyPosition(prcSoFar):
    global currentPos
    (nins, nt) = prcSoFar.shape

    today = prcSoFar[-1]

    rpos = np.array([strategy(instrument, prcSoFar, 7)
                     for instrument in range(nins)])
    currentPos += rpos
    # The algorithm must return a vector of integers, indicating the position of each stock.
    # Position = number of shares, and can be positve or negative depending on long/short position.
    return currentPos
