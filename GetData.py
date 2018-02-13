from dotenv import load_dotenv, find_dotenv
import requests
from requests import session
import os



def extract_data(url, path):
    payload = {
        'action': 'login',
        'username': os.environ.get("KAGGLE_USERNAME"),
        'password': os.environ.get("KAGGLE_PSWD")
    }
    with session() as c:
        c.post('https://kaggle.com/account/login', data=payload)
        with open(path, 'wb') as handle:
            response = c.get(url, stream = True)
            for block in  response.iter_content(1024):
                handle.write(block)

def main(data_dir):
    train_url = 'https://www.kaggle.com/c/titanic/download/train.csv'
    test_url = 'https://www.kaggle.com/c/titanic/download/test.csv'
    raw_data_path = os.path.join(data_dir ,'raw')

    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')

    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)

if __name__ == '__main__':
    data_dir = 'C:\\Users\\amynam\\Documents\\GitHub\\PythonLearning\\titanic\\data'
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    main(data_dir)

