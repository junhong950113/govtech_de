-- Q: I want to find out the top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month


SELECT 
   m.name AS manufacturer,
   COUNT(s.id) AS sales_quantity,
   SUM(s.final_price) AS sales
FROM sales.sales s
INNER JOIN sales.car car
   ON s.car_id = car.id
INNER JOIN sales.car_model cm
   ON car.model_id = cm.id
INNER JOIN sales.manufacturer m
   ON cm.manufacturer_id = m.id
WHERE DATE_PART('month', s.datetime)=DATE_PART('month', CURRENT_TIMESTAMP) AND DATE_PART('year', s.datetime)=DATE_PART('year', CURRENT_TIMESTAMP)
GROUP BY m.id, m.name
ORDER BY sales_quantity DESC, sales DESC
LIMIT 3;