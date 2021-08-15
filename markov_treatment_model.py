import numpy as np
import pandas as pd

CYCLES = 12
STATE_MEMBERSHIP = [1000,0,0] # healthy, diseased, dead

treatment_matrix = {
    'a': [[0.7,0.2,0.1],
            [0.2,0.6,0.2],
            [0,0,1]],
    'b': [[0.4,0.4,0.2],
            [0.1,0.6,0.3],
            [0,0,1]],
}

payoffs = {
    'a': {'cost': [5000,12000,0],
            'utility': [0.6,0.2,0]},
    'b': {'cost': [4000,10000,0],
            'utility': [0.8,0.5,0]},
}

class MarkovModel():
    ''' Instantiate a simple Markov Model '''
    def __init__(self):
        self.membership = list()
        self.treatments = {}
        self.payoffs = {}
        self.cycles = None
        self.results_ = None

    def add_param(self, type, data, name):
        ''' Input a condition or parameter into model '''

        if type == 'treatment':
            self.treatments[name] = data
        elif type == 'cost':
            if name not in self.payoffs.keys():
                self.payoffs[name] = {}
            self.payoffs[name]['cost'] = data
        elif type == 'utility':
            if name not in self.payoffs.keys():
                self.payoffs[name] = {}
            self.payoffs[name]['utility'] = data
        else:
            raise('Option not available. Type should be treatment, cost, or utility.')

        return True

    def _calc_members(self, membership, treatment_name):
        self.membership = membership
        return np.dot(membership, self.treatments[treatment_name])

    def _calc_costs(self, membership, cost_name):
        return np.multiply(membership, self.payoffs[cost_name]['cost']).tolist()

    def _calc_qalys(self, membership, utility_name):
        return np.multiply(membership, self.payoffs[utility_name]['utility']).tolist()

    def run(self, membership, name, cycles):
        ''' Runs model '''

        # Cycle 0
        cycle_membership, cycle_cost, cycle_qaly = membership, self.payoffs[name]['cost'], self.payoffs[name]['utility']
        outcome_membership = [membership]
        outcome_cost = [cycle_cost]
        outcome_qaly = [cycle_qaly]

        for cycle in range(1, cycles):
            cycle_membership = self._calc_members(cycle_membership, name)
            outcome_membership.append(cycle_membership)
            cycle_cost = self._calc_costs(cycle_membership, name)
            outcome_cost.append(cycle_cost)
            cycle_qaly = self._calc_qalys(cycle_membership, name)
            outcome_qaly.append(cycle_qaly)

        self.results_ = {
                'membership': outcome_membership,
                'cost': outcome_cost,
                'qaly': outcome_qaly,
                }
        print(self.results_)
        return self.results_

    def score(self):

        if self.results_ is not None:
            colnames = ['Healthy', 'Diseased', 'Dead']
            print('\nMembership\n')
            print(pd.DataFrame(self.results_['membership'], columns=colnames))
            print('\n--------------------------------------\n')
            print('\nCost\n')
            print(pd.DataFrame(self.results_['cost'], columns=colnames))
            print('\n--------------------------------------\n')
            print('\nUtility\n')
            print(pd.DataFrame(self.results_['qaly'], columns=colnames))
            print('\n--------------------------------------\n')
        else:
            return None

if __name__ == '__main__':

    markov = MarkovModel()
    for treatment in ['a', 'b']:
        markov.add_param('treatment', treatment_matrix[treatment], treatment)
        markov.add_param('cost', payoffs[treatment]['cost'], treatment)
        markov.add_param('utility', payoffs[treatment]['utility'], treatment)
    res = markov.run(STATE_MEMBERSHIP, 'a', CYCLES)
    markov.score()
