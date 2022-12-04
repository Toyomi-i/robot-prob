import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("nbagg")
import matplotlib.animation as anm
import logging

# my func and class
from .Robot import IdealRobot

class World:
    def __init__(self, debug=False, logger=None) -> None:
        # robotなどのオブジェクトを登録
        self.objects: list[IdealRobot] = []
        # デバッグ用フラグ
        self.debug = debug
        self.logger = logger

    # オブジェクト登録用の関数
    def append(self, obj):
        self.objects.append(obj)

    def draw(self, gifname="test.gif"):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111)
        ax.set_aspect("equal")
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_xlabel("X", fontsize=20)
        ax.set_ylabel("Y", fontsize=20)

        # 描画する図形のリスト
        elems = []

        if self.debug:
            # debug時はアニメーションなし
            self.logger.debug("no animation.")
            
            for i in range(1000):
                self.one_step(i, elems, ax)
        else:
            self.logger.debug("make animation.")

            # 引数: 図オブジェクト，1ステップ進める関数，関数に渡す引数，描画する総ステップ数，ステップの周期(ms)，繰り返し表示するか
            self.ani = anm.FuncAnimation(fig, self.one_step, fargs=(elems, ax), frames=10, interval=1000, repeat=False)
            
            # gif保存 plt.showが使えないため(原因分かってない)
            self.ani.save(gifname)


    # animationを1コマ進める
    def one_step(self, i, elems: list, ax: matplotlib.axes):
        # self.logger.debug(f"elems: {elems}")

        # 2重に描画するのを防ぐためにelemsクリア
        while elems:
            elems.pop().remove()

        # 時刻を描画
        elems.append(ax.text(-4.4, 4.5, "t=" + str(i), fontsize=10))

        for obj in self.objects:
            # obj: IdealRobot
            obj.draw(ax, elems)