-- Q:I want to know the list of our customers and their spending

SELECT
   c.name AS customer_name,
   SUM(s.final_price) AS spending
FROM sales.customer c
INNER JOIN sales.sales s
   ON c.id=s.customer_id
GROUP BY c.id, c.name