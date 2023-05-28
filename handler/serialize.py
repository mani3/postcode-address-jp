import argparse
import json
import os
import pickle

import pandas as pd
from tqdm import tqdm

HEADER_NAMES = [
  'jisx0401', 'old_code', 'postal_code',
  'prefecture_kana', 'city_kana', 'town_kana',
  'prefecture', 'city', 'town',
  'town_partial', 'town_koaza', 'town_chome', 'town_multiple', 'update_type', 'update_reason'
]
JSON_KEY_NAMES = ['postal_code', 'prefecture_kana', 'city_kana', 'town_kana', 'prefecture', 'city', 'town']
WITHOUT_TOWN_NAMES = [k for k in JSON_KEY_NAMES if k != 'town_kana']
WITHOUT_TOWN_KANA_NAMES = [k for k in JSON_KEY_NAMES if k != 'town']


def convert_csv(file_path: str):
  df = pd.read_csv(file_path, encoding='shift_jis', names=HEADER_NAMES, header=None, index_col=False, dtype=str)
  zip_codes = list(df['postal_code'].unique())

  addresses = {}
  for zip_code in tqdm(zip_codes):
    address_df = df[(df['postal_code'] == zip_code) & (df['town_multiple'] == '0')].copy(deep=True)
    address_df = address_df[JSON_KEY_NAMES]

    if not address_df.empty:
      if len(address_df) > 1:
        address_df['town_kana'] = address_df.groupby(
          WITHOUT_TOWN_KANA_NAMES)['town_kana'].transform(lambda x: ''.join(x))
        address_df['town'] = address_df.groupby(
          WITHOUT_TOWN_NAMES)['town'].transform(lambda x: ''.join(x))
        address_df = address_df.drop_duplicates()
      else:
        pass
    else:
      address_df = df[df['postal_code'] == zip_code]

    addresses[zip_code] = json.loads(address_df.to_json(orient="records"))
  return addresses


def main(args):
  file_path = args.csv_path
  addresses = convert_csv(file_path)

  basename, _ = os.path.splitext(os.path.basename(file_path))
  output_dir = os.path.dirname(file_path)
  output_path = os.path.join(output_dir, f'{basename.lower()}.pkl')

  with open(output_path, 'wb') as f:
    pickle.dump(addresses, f)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--csv-path", action="store", help="csv file path")
  args = parser.parse_args()
  main(args)
