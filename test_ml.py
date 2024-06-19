import pytest
import pandas as pd
import os
from sklearn.model_selection import train_test_split


@pytest.fixture(scope="session")
def data():
    """
    # create read_data definition to reuse while loading data
    """
    data_path = './data/census.csv'
    df = pd.read_csv(data_path)
    return df


def test_column_count(data):
    """
    # check for 15 expected columns
    """
    assert data.shape[1] == 15


def test_record_count(data):
    """
    # check for expected record count of 32,561
    """
    assert data.shape[0] == 32561


def test_training_size(data):
    """
    # check that training dataset size is 80% of total records
    """
    train, test = train_test_split(data, test_size=0.2, random_state=42)

    train_size = len(train)
    exp_train_size = 26048

    assert train_size == exp_train_size


def test_testing_size(data):
    """
    # check that testing dataset size is 20% of total records
    """
    train, test = train_test_split(data, test_size=0.2, random_state=42)

    test_size = len(test)
    exp_test_size = 6513

    assert test_size == exp_test_size
