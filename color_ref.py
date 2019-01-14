import os
import datetime
import argparse
from collections import OrderedDict

import matplotlib as mpl
print('* loaded matplotlib', mpl.__version__)

import matplotlib.pyplot as plt

cmaps = OrderedDict()
cmaps['Perceptually Uniform Sequential'] = [
      'viridis', 'plasma', 'inferno', 'magma', 'cividis']
cmaps['Sequential'] = [
      'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
cmaps['Sequential (2)'] = [
      'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
      'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
      'hot', 'afmhot', 'gist_heat', 'copper']
cmaps['Diverging'] = [
      'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
      'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
cmaps['Cyclic'] = ['twilight', 'twilight_shifted', 'hsv']
cmaps['Qualitative'] = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
      'Dark2', 'Set1', 'Set2', 'Set3',
      'tab10', 'tab20', 'tab20b', 'tab20c']
cmaps['Miscellaneous'] = [
      'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
      'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
      'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']

def draw_color_ref():
    pass


if __name__ == "__main__":
    draw_color_ref()