def transform_data(**context):
    import pandas as pd

    # Pull from XCom
    data = context['ti'].xcom_pull(key='crypto_data',
        task_ids='extract_data')
    
    df = pd.DataFrame(data)

    # Basic cleaning
    df = df[['id', 'symbol', 'current_price']]
    df = df.drop_duplicates()

    # Push transformed data
    context['ti'].xcom_push(key='transformed_data', value=df.to_dict())