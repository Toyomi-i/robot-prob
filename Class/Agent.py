class Agent:
    def __init__(self, nu, omega) -> None:
        # Agent(ロボットに乗って操作する人, 考える主体)の速度nu, 各速度omega
        self.nu = nu
        self.omega = omega

    def decision(self, observation=None):
        """
        observation: センサ値
        """
        return self.nu, self.omega