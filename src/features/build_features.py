import pandas as pd
import numpy as np

def build_features(df):
    df_feat = df.copy()

    # Total number of guests
    df_feat['total_people'] = df_feat['no_of_adults'] + df_feat['no_of_children']

    # Total number of nights
    df_feat['total_nights'] = df_feat['no_of_weekend_nights'] + df_feat['no_of_week_nights']

    # Price per person
    df_feat['price_per_person'] = df_feat['avg_price_per_room'] / (df_feat['total_people'] + 0.1)

    # Invlolves weekend?
    df_feat['involves_weekend'] = (df_feat['no_of_weekend_nights'] > 0).astype(int)

    # Guest cancellation rate
    df_feat['cancellation_history_rate'] = df_feat['no_of_previous_cancellations'] / (
        df_feat['no_of_previous_cancellations'] + df_feat['no_of_previous_bookings_not_canceled'] + 1
    )

    def get_season(month):
        if month in [12, 1, 2]: return 'Winter'
        if month in [3, 4, 5]: return 'Spring'
        if month in [6, 7, 8]: return 'Summer'
        return 'Autumn'
    
    # Season of arrival
    df_feat['arrival_season'] = df_feat['arrival_month'].apply(get_season)

    # Any special requests?
    df_feat['has_special_requests'] = (df_feat['no_of_special_requests'] > 0).astype(int)

    # Log transformation of lead time
    df_feat['log_lead_time'] = np.log1p(df_feat['lead_time'])

    print(f"New number of features: {df_feat.shape[1]}")
    return df_feat