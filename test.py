import unittest
import numpy as np

from markov_treatment_model import MarkovModel

class TestIllnessDeathModel(unittest.TestCase):
    ''' Tests basic Illness-Death markov model '''

    def setUp(self):
        treatment_matrix = {
            'illness-death': [[0.96,0.03,0.01],
                    [0,0.95,0.05],
                    [0,0,1]],
        }

        payoffs = {
            'illness-death': {'cost': [50,0.9,0],
                    'utility': [0.9,0.6,0]},
        }
        CYCLES = 40
        STATE_MEMBERSHIP = [1000,0,0]
        STATES = ['Healthy','Diseased','Dead']

        markov = MarkovModel()
        for treatment in ['illness-death']:
            markov.set_states(STATES)
            markov.add_param('treatment', treatment_matrix[treatment], treatment)
            markov.add_param('cost', payoffs[treatment]['cost'], treatment)
            markov.add_param('utility', payoffs[treatment]['utility'], treatment)
        self.model_results = markov.run(STATE_MEMBERSHIP, 'illness-death', CYCLES)

    def test_membership(self):
        membership = self.model_results['membership']
        # Membership is 40 cycles long
        self.assertEqual(np.array(membership).shape[0], 40)
        # End membership is correct
        self.assertEqual(np.around(membership[-1],2).tolist(), [203.51,204.69,591.80])

    def test_costs(self):
        costs = self.model_results['cost']
        # Membership is 40 cycles long
        self.assertEqual(np.array(costs).shape[0], 40)
        # End membership is correct
        self.assertEqual(np.around(costs[-1],2).tolist(), [10175.32,184.22,0.00])

    def test_payoffs(self):
        payoffs = self.model_results['qaly']
        # Membership is 40 cycles long
        self.assertEqual(np.array(payoffs).shape[0], 40)
        # End membership is correct
        self.assertEqual(np.around(payoffs[-1],2).tolist(), [183.16,122.81,0.00])


if __name__ == '__main__':
    unittest.main()
