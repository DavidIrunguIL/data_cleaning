from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime as dt
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()



def get_footprint_data_from_db(reg_number):
    try:
        db_host = os.getenv("DB_HOST_UAT")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("FP_DB_NAME")
        driver = os.getenv("DRIVER")
        trusted_conn = os.getenv("TRUSTED_CONN")
        server = os.getenv("SERVER")

        connection_string = (
            f"mssql+pyodbc://{db_host},{db_port}/{db_name}?driver={driver}&trusted_connection={trusted_conn}"
        )
        #SQLAlchemy engine
        engine = create_engine(connection_string)
        logger.info(f"Successfully connected to the footprint DB::")
    except Exception as e:
        logger.error(f'error getting DB credentials:: {e}')

    try:
        reg_str_string = reg_number.replace(' ', '')
        first_ = reg_str_string[:3]
        second_ = reg_str_string[3:]

        query = text('''
            SELECT TOP 1 * 
            FROM ICEALIONVehiclesnew
            WHERE RegistrationNo LIKE :reg_pattern
            order by PeriodFrom DESC;
        ''')
        params = {'reg_pattern': f'%{first_}%{second_}%'}

        with engine.connect() as connection:
            df = pd.read_sql_query(
                query,
                connection,
                params=params
            )
        return df
    except Exception as e:
        logger.error(f'error fetching FP_data{e}')


# print(get_footprint_data_from_db('KDA070'))

