import pandas as pd

def get_synthetic_index(queryset):
    """
    :return: Prices serie of a sinthetic index
    """
    df = get_dataframe(queryset)

    # Underlying security i on date t
    df['rit'] = df['price'] / df['price'].shift() - 1

    # Index on date t
    df['Rt'] = df['weight'] * df['rit']
    df['Rt'] = df['Rt'].drop(index=0).cumsum()

    # Price of the index
    df['Pt'] = df['price'].shift() * (1 + df['Rt'])

    # Remove Nan - first element
    serie_prices =df.Pt.iloc[1:]

    return serie_prices.to_dict()

def get_dataframe(queryset):
    """
    Convert queryset into pandas DataFrame
    """
    df = pd.DataFrame.from_records(queryset.values('weight', 'date', 'price'))
    return df