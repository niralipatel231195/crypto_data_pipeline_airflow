def load_data(**context):
    import psycopg2
    import pandas as pd

    data = context['ti'].xcom_pull(
        key='transformed_data',
        task_ids='transform_data'
    )

    df = pd.DataFrame.from_dict(data)

    conn = psycopg2.connect(
        host="localhost",
        database="crypto_db",
        user="postgres",
        password="postgres123"
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO crypto_prices_v2 (id, symbol, price)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (row['id'], row['symbol'], row['current_price']))

    conn.commit()
    cursor.close()
    conn.close()