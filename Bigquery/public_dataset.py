from google.cloud import bigquery
import sys

def query_public_dataset():
    client = bigquery.Client()

    query = """
    SELECT 
        order_items.id, 
        order_items.order_id, 
        order_items.product_id, 
        products.name
    FROM `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
    JOIN `bigquery-public-data.thelook_ecommerce.products` AS products
    ON order_items.product_id = products.id
    LIMIT 10
    """
    
    #results = client.query(query)
    results = client.query(query).to_dataframe()[:20]

    #for row in results:
        #print(f"{row.id}: {row.name}")

    print(results)

if __name__ == "__main__":
    query_public_dataset()