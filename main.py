import numpy as np
import random
from tqdm import tqdm

np.random.seed(0)
random.seed(0)


def one_cut_random_ex_one(size=1000000):
    a=np.random.uniform(low=0, high=1.01, size=size)

    ans = 0
    # player 1 is 1/2 for 0 to 1/2, 3/2 for 1/2 to 1
    # player 2 is 3/2 for 0 to 1/2, 1/2 for 1/2 to 1
    for x in tqdm(a):
        # player 1 gets piece 1, player 2 gets piece 2
        player_1_utility_sit_1 = min(0, x - 0.5)*3/2.0 + min(0.5, x)*1/2.0
        player_2_utility_sit_1 = (0.5 - min(0, x - 0.5))*1/2.0 + (0.5 - min(0.5, x))*3/2.0

        # player 1 gets piece 2, player 2 gets piece 1
        player_1_utility_sit_2 = (0.5 - min(0, x - 0.5))*3/2.0 + (0.5 - min(0.5, x))*1/2.0
        player_2_utility_sit_2 = min(0, x - 0.5)*1/2.0 + min(0.5, x)*3/2.0

        if player_1_utility_sit_1 >= 0.5 and player_2_utility_sit_1 >= 0.5:
            ans += 1
        elif player_1_utility_sit_2 >= 0.5 and player_2_utility_sit_2 >= 0.5:
            ans += 1

    return (1.0 * ans)/size


if __name__ == "__main__":
    print(one_cut_random_ex_one())
