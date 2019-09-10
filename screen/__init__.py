''' Module for screenshoting '''
import logging
import time

import mss
import mss.tools
import numpy
import win32gui

from settings import MARGIN, MARGIN_TOP


def screenshot(rect):
    ''' Captures window '''
    with mss.mss() as sct:
        left, top, right, bot = rect
        left = left + MARGIN
        top = top + MARGIN_TOP
        width = right - left - MARGIN
        height = bot - top - MARGIN

        monitor = {'top': top, 'left': left, 'width': width, 'height': height}

        sct_img = numpy.array(sct.grab(monitor))
        sct_img = sct_img[:, :, :3]
        return sct_img
