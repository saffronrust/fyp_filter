import pandas as pd

def filter_csv():
    # load file into pd
    df = pd.read_csv('FYP.csv')
    
    # get input for filters
    supervisor_filter = input("Enter name of supervisors, separated by comma (or press enter to skip): ").strip()
    category_filter = input("Enter category names, separated by comma (or press enter to skip): ").strip()
    type_filter = input("Enter types, separated by comma (or press enter to skip): ").strip()
    keywords_filter = input("Enter keywords, separated by comma (or press enter to skip): ").strip()
    
    # get input for blacklist filters
    blacklist_supervisor = input("Enter name of supervisors to exclude, separated by comma (or press enter to skip): ").strip()
    blacklist_category = input("Enter category names to exclude, separated by comma (or press enter to skip): ").strip()
    blacklist_type = input("Enter types to exclude, separated by comma (or press enter to skip): ").strip()
    blacklist_keywords = input("Enter keywords to exclude, separated by comma (or press enter to skip): ").strip()
    
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
