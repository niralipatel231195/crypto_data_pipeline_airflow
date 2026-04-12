def extract_data(**context):
    import requests

    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum"
    }

    response = requests.get(url,params=params)
    data = response.json()

    # Push to XCom
    context['ti'].xcom_push(key='crypto_data', value=data)