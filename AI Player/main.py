from env import Env
from rl import RL

MAX_EPISODES = 1000
MAX_EP_STEPS = 500
ON_TRAIN = True
KEYS = {0:273, 1:274, 2:276, 3:275}
env = Env()
rl = RL(4, 32)

steps = []


def train():
    # start training
    #rl.restore()
    for i in range(MAX_EPISODES):
        s = env.reset()
        ep_r = 0.
        for j in range(MAX_EP_STEPS):
            #env.draw()

            a = rl.choose_action(s)

            s_, r, done = env.step(KEYS[a])

            rl.store_transition(s, a, r, s_)

            ep_r += r
            rl.learn()

            s = s_
            if done or j == MAX_EP_STEPS-1:
                print('Ep: %i | %s | ep_r: %.1f | step: %i' % (i, '---' if not done else 'done', ep_r, j))
                break
    rl.save()


def run():
    rl.restore()
    s = env.reset()
    while True:
        env.draw()
        a = rl.choose_action(s)
        s, _, done = env.step(KEYS[a])
        if done:
            s = env.reset()
            print('running')


if ON_TRAIN:
    train()
else:
    run()

if __name__ == '__main__':
    print('main')
    run()