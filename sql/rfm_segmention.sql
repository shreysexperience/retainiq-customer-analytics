WITH rfm AS (
    SELECT
        c.customer_unique_id,

        MAX(o.order_purchase_timestamp) AS last_purchase,

        (
            SELECT MAX(order_purchase_timestamp)
            FROM orders
        )::date -
        MAX(o.order_purchase_timestamp)::date AS recency,

        COUNT(DISTINCT o.order_id) AS frequency,

        ROUND(SUM(p.payment_value),2) AS monetary

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    JOIN payments p
        ON o.order_id = p.order_id

    GROUP BY c.customer_unique_id
)

SELECT *
FROM rfm
ORDER BY monetary DESC;