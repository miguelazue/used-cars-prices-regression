import pandas as pd
import re

# pd.options.display.float_format = '{:,.2f}'.format
# pd.options.display.float_format = '{:,.0f}'.format


#----------------------------
#--- FUNCTIONS DEFINITION ---
#----------------------------

# Functions to extract different parts associated to the engine

# Extracting HP - Extracts digits before HP, with decimals or with no decimals
def extract_hp(value):
    match = re.search(r'(\d+\.\d+|\d+)HP', value)
    return match.group(1) if match else None
    
# Extracting Engine Size (L) - Extracts digits before L, with decimals or with no decimals
def extract_size(value):
    match = re.search(r'(\d+\.\d+|\d+)L', value)
    return match.group(1) if match else None
    
# Extracting number of cylinders - Extracts digits before Cylinder, with no decimals
def extract_cylinder(value):
    match = re.search(r'(\d+) Cylinder', value)
    return int(match.group(1)) if match else None

def extract_fuel_type(value):
    if 'Hybrid' in value:
        return 'Hybrid'
    elif 'Electric' in value:
        return 'Electric'
    elif 'Gasoline' in value:
        return 'Gasoline'
    elif 'Diesel' in value:
        return 'Diesel'
    else:
        return 'Other'

def extract_engine_config(value):
    if 'V' in value:
        return 'V-Type'
    elif 'I' in value or 'inline' in value:
        return 'Inline'
    elif 'Flat' in value :
        return 'Flat'   
    else:
        return 'Other'
        
def extract_turbo(value):
    # Use re.IGNORECASE for case-insensitive matching
    if re.search(r'turbo', value, re.IGNORECASE):
        return 1
    else:
        return 0
    
# Functions to extract transmission type and number of speeds
# Map transmission type
def map_transmission_type(value):
    if 'M/T' in value or 'Manual' in value or 'Mt' in value:
        return 'Manual'
    elif 'A/T' in value or 'Automatic' in value or 'CVT' in value:
        return 'Automatic'
    elif 'CVT' in value:
        return 'CVT'
    elif 'Dual Shift' in value:
        return 'DCT' 
    else: 
        return 'Other'  # For any unexpected values

# Extract number of speeds
def extract_speeds(value):
    # Regular expression to find the speed number
    import re
    match = re.search(r'(\d+)-Speed', value, re.IGNORECASE)
    if match:
        return int(match.group(1))
    elif 'Single-Speed' in value or '1-Speed' in value:
        return 1
    else:
        return None  # If no speed is found



def transform_cars_df(input_df,df_type="train"):

    transformed_df = input_df.copy()
    transformed_df.columns= transformed_df.columns.str.lower()
    transformed_df.columns = transformed_df.columns.str.replace(' ','_')

    # Binary variables formatting
    #accident and clean title
    transformed_df['vehicle_damage'] = transformed_df['accident'].map({'At least 1 accident or damage reported': 1, 'None reported': 0})

    # Clean title map Yes -> 1 and Blank -> 0
    transformed_df['binary_clean_title'] = transformed_df['clean_title'].apply(lambda x: 1 if x == 'Yes' else 0)


    # extract engine information
    transformed_df['hp'] = transformed_df['engine'].apply(extract_hp)
    transformed_df['size'] = transformed_df['engine'].apply(extract_size)
    transformed_df['cylinder'] = transformed_df['engine'].apply(extract_cylinder)
    transformed_df['fuel_type_2'] = transformed_df['engine'].apply(extract_fuel_type)
    transformed_df['engine_config'] = transformed_df['engine'].apply(extract_engine_config)
    transformed_df['turbo'] = transformed_df['engine'].apply(extract_turbo)

    # extract transmission information
    transformed_df['transmission_type'] = transformed_df['transmission'].apply(map_transmission_type)
    transformed_df['speed'] = transformed_df['transmission'].apply(extract_speeds)


    # Load the mapping from the CSV file
    ext_color_bins_mapping = pd.read_csv('data/ext_color_bins_mapping.csv')
    int_color_bins_mapping = pd.read_csv('data/int_color_bins_mapping.csv')
    brand_bins_mapping = pd.read_csv('data/brand_bins_mapping.csv')

    transformed_df = transformed_df.merge(ext_color_bins_mapping, on='ext_col', how='left')
    transformed_df = transformed_df.merge(int_color_bins_mapping, on='int_col', how='left')
    transformed_df = transformed_df.merge(brand_bins_mapping, on='brand', how='left')

    # Asssigning the most frequent value to NAs
    transformed_df['vehicle_damage'] = transformed_df['vehicle_damage'].fillna(0)
    transformed_df['fuel_type'] = transformed_df['fuel_type'].fillna('Gasoline')
    transformed_df['cylinder'] = transformed_df['cylinder'].fillna(6)
    transformed_df['speed'] = transformed_df['speed'].fillna(6)
    transformed_df['hp'] = transformed_df['hp'].fillna(300)
    transformed_df['size'] = transformed_df['size'].fillna(3)

    # Asssigning na ext_colors, int_color and brands to the most frequent bin: 1
    transformed_df['ext_col_price_bin'] = transformed_df['ext_col_price_bin'].fillna(1)
    transformed_df['int_col_price_bin'] = transformed_df['int_col_price_bin'].fillna(1)
    transformed_df['brand_price_bin'] = transformed_df['brand_price_bin'].fillna(1)


    id_column = ["id"]
    binary_columns = ['vehicle_damage', 'binary_clean_title','turbo']
    categorical_columns_low_cardinality = ['fuel_type_2','engine_config', 'transmission_type','cylinder','speed'] # not using the given fuel type
    ordinal_columns = ['ext_col_price_bin', 'int_col_price_bin', 'brand_price_bin']

    if df_type == "train":
        numeric_columns = ['model_year', 'milage','hp','size','price']
    else:
        numeric_columns = ['model_year', 'milage','hp','size']


    # One hot encoding
    transformed_df = pd.get_dummies(transformed_df, columns=categorical_columns_low_cardinality)

    boolean_columns =['fuel_type_2_Diesel', 'fuel_type_2_Electric', 'fuel_type_2_Gasoline',
       'fuel_type_2_Hybrid', 'fuel_type_2_Other', 'engine_config_Flat',
       'engine_config_Inline', 'engine_config_Other', 'engine_config_V-Type',
       'transmission_type_Automatic', 'transmission_type_DCT',
       'transmission_type_Manual', 'transmission_type_Other', 'cylinder_3.0',
       'cylinder_4.0', 'cylinder_5.0', 'cylinder_6.0', 'cylinder_8.0',
       'cylinder_10.0', 'cylinder_12.0', 'speed_1.0', 'speed_2.0', 'speed_4.0',
       'speed_5.0', 'speed_6.0', 'speed_7.0', 'speed_8.0', 'speed_9.0',
       'speed_10.0']

    # Formating the dummies as 1s and 0s instead of True and False
    #boolean_columns = transformed_df.select_dtypes(include='bool').columns
    transformed_df[boolean_columns] = transformed_df[boolean_columns].astype(int)


    columns_to_use = id_column + binary_columns + boolean_columns + ordinal_columns + numeric_columns


    result_df = transformed_df[columns_to_use]

    for col in columns_to_use:
        na_count = result_df[col].isna().sum()
        print("For column",col,na_count)

    return(result_df)



# Load and transform the train dataset
cars_train_path = 'data/train.csv'
raw_cars_train_df = pd.read_csv(cars_train_path,index_col=None)
cars_train_df = transform_cars_df(raw_cars_train_df,df_type="train")

# Save the transformed data
cars_train_df.to_csv('data/processed_train.csv', index=False)

# Load and transform the train dataset
cars_test_path = 'data/test.csv'
raw_cars_test_df = pd.read_csv(cars_test_path,index_col=None)
cars_test_df = transform_cars_df(raw_cars_test_df,df_type="test")

# Save the transformed data
cars_test_df.to_csv('data/processed_test.csv', index=False)