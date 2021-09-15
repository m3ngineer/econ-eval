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
        self.state_names = self.set_states(['Healthy', 'Diseased', 'Dead'])

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

    def set_states(self, states):
        self.state_names = states

    def _calc_members(self, membership, treatment_name):
        self.membership = membership
        return np.dot(membership, self.treatments[treatment_name]).tolist()

    def _calc_costs(self, membership, cost_name):
        return np.multiply(membership, self.payoffs[cost_name]['cost']).tolist()

    def _calc_qalys(self, membership, utility_name):
        return np.multiply(membership, self.payoffs[utility_name]['utility']).tolist()

    def run(self, membership, name, cycles):
        ''' Runs model '''

        # Cycle 0
        cycle_membership, cycle_cost, cycle_qaly = membership, self.payoffs[name]['cost'], self.payoffs[name]['utility']
        outcome_membership = [membership]
        outcome_cost = np.multiply(outcome_membership, [cycle_cost]).tolist()
        outcome_qaly = np.multiply(outcome_membership, [cycle_qaly]).tolist()

        for cycle in range(1, cycles):
            cycle_membership = self._calc_members(cycle_membership, name)
            outcome_membership.append(cycle_membership)
            cycle_cost = self._calc_costs(cycle_membership, name)
            outcome_cost.append(cycle_cost)
            cycle_qaly = self._calc_qalys(cycle_membership, name)
            outcome_qaly.append(cycle_qaly)

        self.results_ = {
                'name': name,
                'cycles': cycles,
                'membership': outcome_membership,
                'cost': outcome_cost,
                'qaly': outcome_qaly,
                }
        return self.results_

    def _construct_table(self, data, colnames, treatment_names):
        ''' Builds a table of results for comparing treatments '''

        if type(treatment_names) == str:
            treatment_names = [treatment_names]
        result = pd.DataFrame()

        for treatment_name in treatment_names:
            colnames = [col+'_'+treatment_name for col in colnames]
            for i, dat in enumerate(data):
                result = pd.concat([result, pd.DataFrame([dat], columns=colnames)], axis=0)
        return result.reset_index(drop=True).round(2)

    def score(self):

        if self.results_ is not None:
            print('\nMembership\n')
            print(self._construct_table(self.results_['membership'], self.state_names, self.results_['name']))
            print('\n--------------------------------------\n')
            print('\nCost\n')
            print(self._construct_table(self.results_['cost'], self.state_names, self.results_['name']))
            print('\n--------------------------------------\n')
            print('\nUtility\n')
            print(self._construct_table(self.results_['qaly'], self.state_names, self.results_['name']))
            print('\n')

            for metric in ['cost', 'qaly']:
                print(' \nAverage {}:'.format(metric))
                for i, state in enumerate(self.state_names):
                    state_mean = np.around(np.array(self.results_[metric])[:,i].mean(),2)
                    print(' - {}: {}'.format(state, state_mean))
        else:
            return None

    def compare_treatments(self, model1, model2):
        ''' Given a set of parameters get the best model '''

        colnames = ['Healthy', 'Diseased', 'Dead']
        for metric in ['membership', 'cost', 'qaly']:
            res = self._construct_table(model1[metric], colnames, model1['name'])
            res2 = self._construct_table(model2[metric], colnames, model2['name'])

            print('\n{}'.format(metric.title()))
            print('\n--------------------------------------\n')
            print(pd.concat([res, res2], axis=1))

if __name__ == '__main__':

    #aducanumab settings
    # https://link.springer.com/article/10.1007%2Fs40120-021-00273-0#Sec25
    # healthy, MCI due to AD, mild AD, moderate AD, severe AD
    treatment_matrix = {
        'soc': [[0.77,0.23,0,0],
                [0.03,0.58,0.35,0.04],
                [0,0.03,0.55,0.42],
                [0,0,0.02,0.98]],
        'aducanumab': [[0.532,0.318,0.166],
                [0.1,0.6,0.3],
                [0,0,1]],
    }

    # MCI, Mild AD dementia, moderate AD dementia, Severe AD dementia
    payoffs = {
        'soc': {'cost': [5000,12000,0],
                'utility': [0.73,0.68,0.54,0.37]},
        'aducanumab': {'cost': [34825,34825,34825,34825,34825],
                'utility': [0.8,0.74,0.59,0.36,0.00]},
    }
    CYCLES = 10 #years


    markov = MarkovModel()
    for treatment in ['a', 'b']:
        markov.add_param('treatment', treatment_matrix[treatment], treatment)
        markov.add_param('cost', payoffs[treatment]['cost'], treatment)
        markov.add_param('utility', payoffs[treatment]['utility'], treatment)
    m1 = markov.run(STATE_MEMBERSHIP, 'a', CYCLES)
    markov.score()

    m2 = markov.run(STATE_MEMBERSHIP, 'b', CYCLES)
    # markov.score()
    print(markov.compare_treatments(m1, m2))
