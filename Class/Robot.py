import numpy as np
import math
import matplotlib.patches as patches
import matplotlib
import logging
import sys

# my func and class
from .debug_class import init_logger_for_class
from .Agent import Agent

class IdealRobot:
    def __init__(self, pose: np.ndarray, agent: Agent=None, color="black") -> None:
        """
        pose:   ロボットの姿勢．[x, y, theta(rad)]
        agent:  ロボットを操縦する人
        color:  ロボットの色
        """
        
        self.pose = pose
        # robotの向きを表すための直線の長さ
        self.r = 0.2
        self.agent = agent
        self.color = color
        # 軌跡の描画用
        self.poses = [pose]

        # debug
        self.logger = init_logger_for_class(f"robo_{color}", logging.DEBUG)
        


    def draw(self, ax:matplotlib.axes, elems: list) -> None:
        # 姿勢
        x, y, theta = self.pose
        # 向き描画のための値
        xn = x + self.r * math.cos(theta)
        yn = y + self.r * math.sin(theta)

        # ------------------------------------------------------------------------------------------
        # elemあり
        # 向き描画
        elems += ax.plot([x, xn], [y, yn], color=self.color)

        # ロボットの胴体を表す円
        c = patches.Circle(xy=(x, y), radius=self.r, fill=False, color=self.color)
        elems.append(ax.add_patch(c)) 
        # ------------------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------------------
        # p.72追記
        # debug
        # self.poses.append(self.pose)
        # self.logger.debug(f"poses: {self.poses}")
        # self.logger.debug(f"x: {[e[0] for e in self.poses]}")
        # self.logger.debug(f"y: {[e[1] for e in self.poses]}")

        elems += ax.plot([e[0] for e in self.poses], [e[1] for e in self.poses], linewidth=0.5, color="black")
        # ------------------------------------------------------------------------------------------


    # p.70 の実装
    # 世界座標系での現姿勢poseから速度mu, 角速度omega, 時間timeで移動した後の姿勢を計算
    @classmethod
    def state_transtion(cls, nu, omega, time, pose) -> None:
        t0 = pose[2]

        # 角速度がほぼゼロのとき
        if math.fabs(omega) < 1e-10:
            return pose + np.array([
                nu*math.cos(t0),
                nu*math.sin(t0),
                omega
            ]) * time
        # 角速度が0でないとき
        else:
            return pose + np.array([
                nu/omega*(math.sin(t0 + omega*time) - math.sin(t0)),
                nu/omega*(math.cos(t0 + omega*time) - math.cos(t0)),                
                omega*time
            ])

    # agentのdecisionメソッドでロボットを動かす
    def one_step(self, time_interval) -> None:
        if not self.agent: 
            return
        
        nu, omega = self.agent.decision()
        self.pose = self.state_transtion(nu, omega, time_interval, self.pose)
