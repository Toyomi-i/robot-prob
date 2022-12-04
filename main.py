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
from Class.Agent import Agent

from debug import init_logger


logger = init_logger("main", logging.DEBUG)

world = World(logger=logger)
# 0.2[m/s]で直進
straight = Agent(0.2, 0.0)
# 0.2[m/s], 10[deg/s]で移動
circling = Agent(0.2, 10.0/180*math.pi)


# # robotインスタンス
robot1 = IdealRobot(pose=np.array([2, 3, math.pi/6]).T, agent=straight)
robot2 = IdealRobot(pose=np.array([-2, 1, math.pi/5*6]).T, agent=circling, color="red")
robot3 = IdealRobot(pose=np.array([0, 0, 0]).T, color="blue")

# worldに追加
world.append(robot1)
world.append(robot2)
world.append(robot3)


# ロボットのアニメーション描画，gif保存
world.draw()
