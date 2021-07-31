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
    'a': {'costs': [5000,12000,0],
            'utility': [0.6,0.2,0]},
    'b': {'costs': [4000,10000,0],
            'utility': [0.8,0.5,0]},
}

def calc_members(membership, treatment_matrix):
    return np.dot(membership, treatment_matrix)

def calc_costs(membership, costs):
    return np.multiply(membership, costs).tolist()

def calc_qalys(membership, qalys):
    return np.multiply(membership, qalys).tolist()

# Cycle 0
memberships = [STATE_MEMBERSHIP]
costs = [payoffs['a']['costs']]
qalys = [payoffs['a']['utility']]
cycle_membership, cycle_costs, cycle_qalys = STATE_MEMBERSHIP, costs, qalys

for cycle in range(1, CYCLES):
    cycle_membership = calc_members(cycle_membership,treatment_matrix['a'])
    memberships.append(cycle_membership)
    cycle_costs = calc_costs(cycle_membership, payoffs['a']['costs'])
    costs.append(cycle_costs)
    cycle_qalys = calc_qalys(cycle_membership, payoffs['a']['utility'])
    qalys.append(cycle_qalys)

result = {
    'membership': memberships,
    'costs': costs,
    'qalys': qalys,
}
