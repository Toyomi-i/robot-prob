import numpy as np
import math
import matplotlib.patches as patches
import matplotlib

class IdealRobot:
    def __init__(self, pose: np.ndarray, color="black") -> None:
        """
        pose: ロボットの姿勢．[x, y, theta(rad)]
        """
        
        # 初期姿勢
        self.pose = pose
        # robotの向きを表すための直線の長さ
        self.r = 0.2
        self.color = color

    def draw(self, ax:matplotlib.axes, elems: list):
        # 姿勢
        x, y, theta = self.pose
        # 向き描画のための値
        xn = x + self.r * math.cos(theta)
        yn = y + self.r * math.sin(theta)

        # ------------------------------------------------------------------------------------------
        # elemなし
        # # 向き描画
        # ax.plot([x, xn], [y, yn], color=self.color)

        # # ロボットの胴体を表す円
        # c = patches.Circle(xy=(x, y), radius=self.r, fill=False, color=self.color)
        # ax.add_patch(c)
        # ------------------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------------------
        # elemあり
        # 向き描画
        elems += ax.plot([x, xn], [y, yn], color=self.color)

        # ロボットの胴体を表す円
        c = patches.Circle(xy=(x, y), radius=self.r, fill=False, color=self.color)
        elems.append(ax.add_patch(c)) 
        # ------------------------------------------------------------------------------------------

    # p.70 の実装
    # 世界座標系での現姿勢poseから速度mu, 角速度omega, 時間timeで移動した後の姿勢を計算
    @classmethod
    def state_transtion(cls, nu, omega, time, pose):
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