import pandas as pd

def filter_csv():
    # load file into pd
    df = pd.read_csv('FYP.csv')

    def get_unique_values(column_name):
        """Helper function to get unique values from a specific column."""
        if column_name == 'Keywords':
            # TBD
            # since the keyword column is just a string of keywords seperated by space
            # its not possible to distinguish whether each space belong within a keyword or is a sepeator for keywords
            # the input data has to be updated
            return ["TBD"]
        elif column_name in df.columns:
            return df[column_name].dropna().unique()
        return []

    def get_filter_input(prompt, column_name):
        """Helper function to handle user input and display unique values if '?' is entered."""
        while True:
            user_input = input(prompt).strip()
            if user_input == '?':
                unique_values = get_unique_values(column_name)
                print(f"Possible values for {column_name}: {', '.join(map(str, unique_values))}")
                print()

            else:
                return user_input
               
    # get input for filters
    supervisor_filter = get_filter_input(
        "Enter name of supervisors, separated by comma (or press enter to skip, '?' to list options): ", 
        'Supervisor'
    )
    category_filter = get_filter_input(
        "Enter category names, separated by comma (or press enter to skip, '?' to list options): ", 
        'Category'
    )
    type_filter = get_filter_input(
        "Enter types, separated by comma (or press enter to skip, '?' to list options): ", 
        'Type'
    )
    keywords_filter = get_filter_input(
        "Enter keywords, separated by comma (or press enter to skip, '?' to list options): ",
        'Keywords'
    )
    
    # get input for blacklist filters
    blacklist_supervisor = get_filter_input(
        "Enter name of supervisors to exclude, separated by comma (or press enter to skip, '?' to list options): ", 
        'Supervisor'
    )
    blacklist_category = get_filter_input(
        "Enter category names to exclude, separated by comma (or press enter to skip, '?' to list options): ", 
        'Category'
    )
    blacklist_type = get_filter_input(
        "Enter types to exclude, separated by comma (or press enter to skip, '?' to list options): ", 
        'Type'
    )
    blacklist_keywords = get_filter_input(
        "Enter keywords to exclude, separated by comma (or press enter to skip, '?' to list options): ", 
        'Keywords'
    )
    
    # apply inclusion filters
    if supervisor_filter:
        supervisor_filters = supervisor_filter.split(',')
        df = df[df['Supervisor'].apply(lambda x: any(sf.strip().lower() in str(x).lower() for sf in supervisor_filters))]
    if category_filter:
        category_filters = category_filter.split(',')
        df = df[df['Category'].apply(lambda x: any(cf.strip().lower() in str(x).lower() for cf in category_filters))]
    if type_filter:
        type_filters = type_filter.split(',')
        df = df[df['Type'].apply(lambda x: any(tf.strip().lower() in str(x).lower() for tf in type_filters))]
    if keywords_filter:
        keywords = keywords_filter.split(',')
        df = df[df['Keywords'].apply(lambda x: any(kw.strip().lower() in str(x).lower() for kw in keywords))]
    
    # apply blacklist filters
    if blacklist_supervisor:
        blacklist_supervisors = blacklist_supervisor.split(',')
        df = df[~df['Supervisor'].apply(lambda x: any(bs.strip().lower() in str(x).lower() for bs in blacklist_supervisors))]
    if blacklist_category:
        blacklist_categories = blacklist_category.split(',')
        df = df[~df['Category'].apply(lambda x: any(bc.strip().lower() in str(x).lower() for bc in blacklist_categories))]
    if blacklist_type:
        blacklist_types = blacklist_type.split(',')
        df = df[~df['Type'].apply(lambda x: any(bt.strip().lower() in str(x).lower() for bt in blacklist_types))]
    if blacklist_keywords:
        blacklist_kw = blacklist_keywords.split(',')
        df = df[~df['Keywords'].apply(lambda x: any(bk.strip().lower() in str(x).lower() for bk in blacklist_kw))]
    
    # save to csv
    df.to_csv('filtered_fyp.csv', index=False)
    print("Filtered data saved to 'filtered_fyp.csv'.")

if __name__ == "__main__":
    filter_csv()
