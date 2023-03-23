import pandas as pd
import logging

class CleaningDataframe():

    """ A class for cleaning and processing data in a pandas DataFrame """

    useless_columns = ['id', 'conversion', 'fare', 'bags_price', 'baglimit', 'route', 'booking_token',  
        'facilitated_booking_available','technical_stops', 'throw_away_ticketing', 'hidden_city_ticketing', 
        'virtual_interlining', 'utc_arrival', 'utc_departure', 'local_arrival', 'local_departure', 'pnr_count']

    def __init__(self, dataframe: pd.DataFrame) -> None:
        
        self.dataframe = dataframe

        self.extract_data_from_disctionary('countryFrom', 'name')
        self.extract_data_from_disctionary('countryTo', 'name')
        self.extract_data_from_disctionary('duration', 'total')
        self.extract_data_from_disctionary('availability', 'seats')

        self.convert_to_strftime('date_arrival', 'local_arrival')
        self.convert_to_strftime('date_departure', 'local_departure')

        self.delete_useless_columns()
       
    def delete_useless_columns(self):
        """ Delete columns from the DataFrame that are not useful for analysis """
        try:
            self.dataframe.drop(columns=self.useless_columns, inplace=True)
        except Exception as ex: 
            logging.error(f"Error with function delete_useless_columns(): {ex}")

    def extract_data_from_disctionary(self, column_name, dict_value):
        """ Extract a value from a dictionary column in the DataFrame and replace the column with the extracted value """
        self.dataframe[column_name] = self.dataframe[column_name].str.get(dict_value)
    
    def convert_to_strftime(self, new_column_name, column_name):
        """ Convert date into the right date type format 'Y-%m-%d %H:%M' """
        self.dataframe[new_column_name] = pd.to_datetime(self.dataframe[column_name], format="%Y-%m-%dT%H:%M:%S.%fZ")
        self.dataframe[new_column_name] = self.dataframe[new_column_name].dt.strftime('%Y-%m-%d %H:%M')

    def get_clean_data(self):
        """ Return the cleaned DataFrame """
        return self.dataframe.copy()
