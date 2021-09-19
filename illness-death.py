
import numpy as np

from markov_treatment_model import MarkovModel
from utils import randomize_probabilities

# https://www.youtube.com/watch?v=6L5LPkzvbtI&list=PLIT7NqYN7YT0AqAysKJVCwWxrbYGA3quv&index=4&t=2s&ab_channel=Decisionanalyticmodellinginhealtheconomics

if __name__ == '__main__':

    params = {
        'illness-death': {
            'probabilities': [
                    [0.96,0.03,0.01],
                    [0,0.95,0.05],
                    [0,0,1]
                ],
            'cost': [50,0.9,0],
            'utility': [0.9,0.6,0]
        },
    }
    CYCLES = 40
    STATE_MEMBERSHIP = [1000,0,0]
    STATES = ['Healthy','Diseased','Dead']
    RANDOMIZE_PROBABILITIES = True
    
    markov = MarkovModel()
    for treatment in ['illness-death']:
        markov.set_states(STATES)
        markov.add_param('treatment', params[treatment]['probabilities'], treatment)
        markov.add_param('cost', params[treatment]['cost'], treatment)
        markov.add_param('utility', params[treatment]['utility'], treatment)
    m1 = markov.run(STATE_MEMBERSHIP, 'illness-death', CYCLES)
    markov.score()
