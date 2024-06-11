import pandas as pd


def calculate_wrong_outliers(data):
    """
    Calculate outliers (=wrong data) based on the given data.
    """
    # Calculate mean births per day
    births_per_day_mean = data.mean()
    print(f"Gemiddeld aantal geboortes per dag: {births_per_day_mean:.1f}")

    # Calculate the thresholds for outliers (50% deviation)
    lower_outlier_threshold = births_per_day_mean - 0.5 * births_per_day_mean
    upper_outlier_threshold = births_per_day_mean + 0.5 * births_per_day_mean
    print(f"Lower outlier threshold: {lower_outlier_threshold:.1f} ; "
          f"Upper outlier threshold: {upper_outlier_threshold:.1f}")

    # Find outliers based on the conditions
    outliers = data[(data < lower_outlier_threshold) | (data > upper_outlier_threshold)]

    return outliers


def handle_wrong_outliers(data, outliers, reason, df_wrong):
    """
    Handle outliers by moving them to a separate DataFrame and adding a reason for being wrong.
    """
    # Filter rows where the date matches one of the outliers
    rows_to_move = data[data['dag_geboorte'].isin(outliers)]

    # Drop the column 'dag_geboorte' from rows_to_move
    rows_to_move = rows_to_move.drop(columns='dag_geboorte')

    # Add these rows to df_wrong with the reason for being wrong
    rows_to_move['reden foutief'] = reason
    df_wrong_extended = pd.concat([df_wrong, rows_to_move], ignore_index=True)

    # Remove these rows from the original DataFrame
    cleaned_data = data[~data['dag_geboorte'].isin(outliers)]

    return cleaned_data, df_wrong_extended


def calculate_other_outliers(data):
    """
    Calculate outliers (=non-wrong data) based on the given data.
    """
    # Grouping by 'datum_geboorte' and calculating the number of records
    grouped_counts = data.groupby('datum_geboorte').size()

    # Calculate the mean and standard deviation
    mean = grouped_counts.mean()
    std_dev = grouped_counts.std()

    # Calculate z-scores
    z_scores = (grouped_counts - mean) / std_dev

    # Find outliers based on the criterion: if the deviation is greater than 2.5 z-scores.
    # I'm only considering one-sided outliers, specifically those representing lower values.
    outliers = grouped_counts[z_scores < -2.5].reset_index().rename(columns={0: 'aantal geboortes'})

    return outliers
