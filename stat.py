def apply_group_stats_to_test(train, test, group_column):

    # Calculate group-wise means and std on the training dataset
    group_stats = train.groupby(group_column)['CI_HOUR'].agg(['mean', 'std'])

    # Apply these statistics to both the training and test datasets
    train = train.join(group_stats, on=group_column, how='left', rsuffix='_r')
    test = test.join(group_stats, on=group_column, how='left', rsuffix='_r')

    # Rename columns for clarity
    train.rename(columns={'mean_r': f'{group_column}_mean', 'std_r': f'{group_column}_std'}, inplace=True)
    test.rename(columns={'mean_r': f'{group_column}_mean', 'std_r': f'{group_column}_std'}, inplace=True)

    return train, test
