SELECT
    ROUND(SUM(payment_value), 2) AS total_revenue
FROM payments;

SELECT
    COUNT(*) AS total_orders
FROM orders;

SELECT
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM customers;

SELECT
    ROUND(AVG(order_total), 2) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(payment_value) AS order_total
    FROM payments
    GROUP BY order_id
) t;

SELECT
    c.customer_state,
    ROUND(SUM(p.payment_value),2) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN payments p
ON o.order_id=p.order_id
GROUP BY c.customer_state
ORDER BY revenue DESC;

SELECT
    c.customer_city,
    ROUND(SUM(p.payment_value),2) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN payments p
ON o.order_id=p.order_id
GROUP BY c.customer_city
ORDER BY revenue DESC
LIMIT 10;

SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
    ROUND(SUM(p.payment_value),2) AS revenue
FROM orders o
JOIN payments p
ON o.order_id=p.order_id
GROUP BY month
ORDER BY month;

SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;

SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS revenue
FROM payments
GROUP BY payment_type
ORDER BY revenue DESC;

SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;