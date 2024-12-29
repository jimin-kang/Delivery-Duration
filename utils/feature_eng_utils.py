# Determine which percentile the element falls into
def encode_frequency(freq, percentiles) -> str:
    '''
    Description:
        Given a frequency count and associated frequency percentiles, 
        classify the frequency count into one of the following 5 bins and return it.
            - [0-50) percentile
            - [50-75) percentile
            - [75-90) percentile
            - [90-99) percentile
            - 99+ percentile
    Parameters:
        freq: frequency count
        percentiles: array of values defining the bounds for the percentile bins
    Output:
        Percentile bin corresponding w/ freq
    '''
    if freq < percentiles[0]:
        return '[0-50)'
    elif freq < percentiles[1]:
        return '[50-75)'
    elif freq < percentiles[2]:
        return '[75-90)'
    elif freq < percentiles[3]:
        return '[90-99)'
    else:
        return '99+'
    

def map_to_category_type(category: str) -> str:
    '''
    Description:
        Given a store_primary_category, map it to the broader store category type it corresponds to as defined in the mapping below.
    Parameters:
        category: store_primary_category value
    Output:
        store_category_type corresponding to category
    '''
    store_category_map = {
        'american': ['american', 'burger', 'sandwich', 'barbeque'],
        'asian': ['asian', 'chinese', 'japanese', 'indian', 'thai', 'vietnamese', 'dim-sum', 'korean', 
                'sushi', 'bubble-tea', 'malaysian', 'singaporean', 'indonesian', 'russian'],
        'mexican': ['mexican'],
        'italian': ['italian', 'pizza'],
    }

    for category_type, categories in store_category_map.items():
        if category in categories:
            return category_type
    return "other"
  


