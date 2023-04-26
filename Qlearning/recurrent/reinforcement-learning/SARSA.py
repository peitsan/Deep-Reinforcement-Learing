# 复现SARSA 时序 4.27


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#棋盘长宽度
HEIGHT = 10
WIDTH = 10

# 每一列的权重
WIND = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

#动作编号

ACT_UP = 0
ACT_LEFT = 1
ACT_DOWN = 2
ACT_RIGHT = 3

#发现概率

EPSILON = 0.1

#SARSA 步长

ALPHA = 0.5

#动作奖励系数

REWARD = -1

# 初始化

START = [3, 0]
GOAL = [3, 7]

ACTS = [ACT_UP, ACT_LEFT,ACT_DOWN,ACT_RIGHT]


#传入当前坐标状态state 和下一步的动作
# 上下运动列数 j 不变 左右运动行数 i 不变
def step(state, act):
    i, j = state
    if act == ACT_UP: #向上一步
        return [max(i - 1  - WIND[j], 0), j] #比较权值决定是否能向上一步 , 列数不变
    elif act == ACT_LEFT:
        return [max(i - WIND[j], 0), max(j - 1, 0)]
    elif act == ACT_DOWN:
        return [max(min( i + 1 - WIND[j], HEIGHT - 1), 0), j]
    elif act == ACT_RIGHT:
        return [max(i - WIND[j],0), min(j + 1, WIDTH  - 1)] # 向右向下不能溢出
    else:
        assert False

#迭代训练函数
def episode(q_value):
    time = 0
    state = START
    # 按照EPSILON期望, 1次实验随机生成一个服从二项分布的整数, 当为1时, 随机进行一次移动
    if np.random.binomial(1, EPSILON) == 1:
        act = np.random.choice(ACTS)
    else:
        # 当迭代不进行时 比较状态价值和动作价值
        _values = q_value[state[0], state[1], :]  #用当前状态计算价值
        act = np.random.choice([act for act, _value in enumerate(_values) if _value == np.max(_values)])

    while state != GOAL:
        next_state = step(state, act)
        if np.random.binomial(1, EPSILON) == 1:
            next_action = np.random.choice(ACTS)
        else:
            _values = q_value[next_state[0], next_state[1], :]
            next_action = np.random.choice([_act for _act, _value in enumerate(_values) if _value == np.max(_values)])
           # act = np.random.choice([_act for _act, _value in enumerate(_values) if _value == np.max(_values)])
        # 更新 SARSA
        q_value [state[0], state[1], act] +=  \
        ALPHA *(REWARD + q_value[next_state[0], next_state[1], next_action] - q_value[state[0], state[1], act])
        state = next_state
        act = next_action
        time += 1
    return time

def SARSA():
    episode_limit = 500
    q_value = np.zeros((HEIGHT,WIDTH,4))
    # episode(8000) 没有这一句

    steps = []
    ep = 0
    while ep <  episode_limit:
        steps.append(episode(q_value))
        ep += 1

    plt.plot(steps, np.arange(1, len(steps) + 1))
    plt.xlabel('Time steps')
    plt.ylabel('Episodes')

    plt.savefig('./sarsa.png')
    plt.close()

    opimal  = []
    for i in range(0, HEIGHT):
        opimal.append([])
        for j in range(0, WIDTH):
            if[i, j] == GOAL:
                opimal[-1].append('G')
                continue
            bestAct = np.argmax(q_value[i, j, :])
            if bestAct == ACT_UP:
                opimal[-1].append('U');
            elif bestAct == ACT_DOWN:
                opimal[-1].append('D');
            elif bestAct == ACT_LEFT:
                opimal[-1].append('L');
            elif bestAct == ACT_RIGHT:
                opimal[-1].append('R');

    print("接龙库得出方案:")
    for row in opimal:
        print(row)
    print('Wind strength for eact column: \n{}'.format([str(w) for  w in WIND]))

if __name__ == '__main__':
    SARSA()
