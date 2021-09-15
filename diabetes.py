
import numpy as np

from markov_treatment_model import MarkovModel


# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6944539/
# 45-60 y/o
# H1b < 7.5%, 7.5%<=H1b<=9.0%, H1b>9.0%
if __name__ == '__main__':

    treatment_matrix = {
        '45-60yo': [[0.83,0.15,0.02],
                [0.81,0.17,0.02],
                [0.11,0.23,0.66]],
    }

    payoffs = {
        '45-60yo': {'cost': np.dot([3264.30,3264.30,3264.30], 4).tolist(), # 3 month costs (RMB) so multiply for annual costs
                'utility': [0.859,0.859,0.859]},
    }
    CYCLES = 5
    STATE_MEMBERSHIP = [1000,0,0]
    STATES = ["<7.5","7.5<=H1b<=9.0",">9.0"]


    markov = MarkovModel()
    for treatment in ['45-60yo']:
        markov.set_states(STATES)
        markov.add_param('treatment', treatment_matrix[treatment], treatment)
        markov.add_param('cost', payoffs[treatment]['cost'], treatment)
        markov.add_param('utility', payoffs[treatment]['utility'], treatment)
    m1 = markov.run(STATE_MEMBERSHIP, '45-60yo', CYCLES)
    markov.score()
