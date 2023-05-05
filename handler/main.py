import json
import pickle

PICKLE_PATH = './assets/ken_all.pkl'
with open(PICKLE_PATH, 'rb') as f:
  postal_code_addresses = pickle.load(f)


def handler(event, context):
  postal_code = event['pathParameters']['postal_code']
  address = postal_code_addresses.get(postal_code, None)

  if address is None:
    return {
      'statusCode': 404,
      'body': json.dumps({
        'message': 'Not Found'
      }, ensure_ascii=False)
    }

  return {
    'statusCode': 200,
    'body': json.dumps({
      'message': 'OK',
      'data': address
    }, ensure_ascii=False)
  }
