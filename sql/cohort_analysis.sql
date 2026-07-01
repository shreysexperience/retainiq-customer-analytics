SELECT
    c.customer_unique_id,
    MIN(DATE_TRUNC('month', o.order_purchase_timestamp)) AS cohort_month
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
ORDER BY cohort_month;

SELECT
    c.customer_unique_id,
    DATE_TRUNC('month', o.order_purchase_timestamp) AS order_month
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY customer_unique_id;

WITH first_purchase AS
(
    SELECT
        c.customer_unique_id,
        MIN(DATE_TRUNC('month', o.order_purchase_timestamp)) AS cohort_month
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)

SELECT
    fp.customer_unique_id,
    fp.cohort_month,
    DATE_TRUNC('month', o.order_purchase_timestamp) AS order_month
FROM first_purchase fp
JOIN customers c
ON fp.customer_unique_id = c.customer_unique_id
JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY fp.customer_unique_id;

WITH first_purchase AS
(
    SELECT
        c.customer_unique_id,
        MIN(DATE_TRUNC('month', o.order_purchase_timestamp)) AS cohort_month
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)

SELECT
    fp.customer_unique_id,
    fp.cohort_month,
    DATE_TRUNC('month', o.order_purchase_timestamp) AS order_month,

    (
        EXTRACT(YEAR FROM AGE(
            DATE_TRUNC('month', o.order_purchase_timestamp),
            fp.cohort_month
        )) * 12
        +
        EXTRACT(MONTH FROM AGE(
            DATE_TRUNC('month', o.order_purchase_timestamp),
            fp.cohort_month
        ))
    ) AS month_number

FROM first_purchase fp
JOIN customers c
ON fp.customer_unique_id = c.customer_unique_id
JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY fp.customer_unique_id;

WITH first_purchase AS (
    SELECT
        c.customer_unique_id,
        MIN(DATE_TRUNC('month', o.order_purchase_timestamp)) AS cohort_month
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
),

customer_orders AS (
    SELECT
        c.customer_unique_id,
        DATE_TRUNC('month', o.order_purchase_timestamp) AS order_month
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
),

cohort_data AS (
    SELECT
        fp.customer_unique_id,
        fp.cohort_month,
        co.order_month,
        (
            EXTRACT(YEAR FROM AGE(co.order_month, fp.cohort_month)) * 12 +
            EXTRACT(MONTH FROM AGE(co.order_month, fp.cohort_month))
        ) AS cohort_index
    FROM first_purchase fp
    JOIN customer_orders co
        ON fp.customer_unique_id = co.customer_unique_id
)

SELECT
    cohort_month,
    cohort_index,
    COUNT(DISTINCT customer_unique_id) AS customers
FROM cohort_data
GROUP BY
    cohort_month,
    cohort_index
ORDER BY
    cohort_month,
    cohort_index;