##from mySql - - > read it in local - - > Train test split - - > dataset
import os #(so that i can make current path and jo bhi folders and all)
import sys #(for handling Custom exception and logging bhi)
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd



from dataclasses import dataclass 
#dataclasses yaha isly use kar rahe h kuki jo input parameters humko dena h usse hum yaha initilaize kardege


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.joins('artifacts','train.csv')
    test_data_path:str=os.path.joins('artifacts','test.csv')
    raw_data_path:str=os.path.joins('artifacts','raw.csv')


   