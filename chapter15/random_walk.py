from random import choice


class RandomWalk:
    '''一个生成随机漫步数据的类'''

    def __init__(self, num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points

        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步包含的所有点'''

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        # 决定前进方向以及沿这个方向前进的距离
        _direction = choice([1, -1])

        _distance = choice(range(9))
        _step = _direction * _distance
        return _step
