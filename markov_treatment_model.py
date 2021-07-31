import numpy as np

CYCLES = 12
STATE_MEMBERSHIP = {
    'healthy': 1000,
    'diseased': 0,
    'dead': 0,
}

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

def cycle_members(membership, treatment_matrix):
    return np.dot(membership, treatment_matrix)

def cycle_costs(membership, costs):
    return np.multiply(membership, costs)

def cycle_qalys(membership, qalys):
    return np.multiply(membership, qalys)

print(cycle_members([1000,0,0],treatment_matrix['a']))
print(cycle_costs([1000,0,0], payoffs['a']['costs']))
print(cycle_qalys([1000,0,0], payoffs['a']['utility']))
