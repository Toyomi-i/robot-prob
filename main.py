import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
import numpy as np
import matplotlib
matplotlib.use("nbagg")
import matplotlib.animation as anm
import logging


# my func and class
from Class.World import World
from Class.Robot import IdealRobot

from debug import init_logger


logger = init_logger("logger", logging.DEBUG)

world = World(logger=logger)
# world = World(debug=True)
# world.draw()


# # robotインスタンス
robot1 = IdealRobot(np.array([2, 3, math.pi/6]).T)
robot2 = IdealRobot(np.array([-2, 1, math.pi/5*6]).T, "red")

# worldに追加
world.append(robot1)
world.append(robot2)

# ロボットのアニメーション描画，gif保存
world.draw()
