import numpy as np

def randomize_probabilities(data, distribution='beta'):

    if distribution == 'beta':
        return return np.random.beta(data,1-data)
    elif distribution == 'gamma':
        return np.random.gamma((1/0.2)**2, data/(1/0.2)**2)
    else:
        raise('Please pick a distribution (beta, gamma).')
