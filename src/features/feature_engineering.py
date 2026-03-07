
def build_features(df):

    df['month'] = df['date'].dt.month
    df['dayofyear'] = df['date'].dt.dayofyear

    df['temp_humidity_interaction'] = df['temperature_c'] * df['humidity_percent']

    return df
