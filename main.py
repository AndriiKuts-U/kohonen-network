from network import *
from data import *
from plot import *
from random import choice, seed

seed(0)

focals = [[0, 0],
	      [4, 4],
	      [8, 8],[1, 1],[7, 7],[3, 3],[0,8]]

data = GenerateData(focals)

network = Network(5, 5)
network.data = data

plot = Plot()
plot.Scatter(data)
plot.Scatter(network.Unpack())
plot.Show()

network.Train(10000)
network.classificate(1.8)
plot.Scatter(data)
plot.Scatter(network.Unpack())
plot.Show()
