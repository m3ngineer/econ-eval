import numpy as np
import pandas as pd

def randomize_probabilities(data, distribution='beta'):

    def fmt_data(data):
        ''' Formats data into Pandas Series if not already '''
        if (type(data) == float) or (type(data) == int):
            data = [data]
        return pd.Series(data)

    data = fmt_data(data)
    if distribution == 'beta':
        return data.apply(lambda x: np.around(np.random.beta(x,1-x),4)).tolist()
    elif distribution == 'gamma':
        return data.apply(lambda x: np.around(np.random.gamma((1/0.2)**2, data/(1/0.2)**2),4)).tolist()
    else:
        raise('Please pick a distribution (beta, gamma).')
