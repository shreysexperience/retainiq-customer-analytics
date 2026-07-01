# RetainIQ – SQL Business Query Results

## Query 1 – Total Revenue

**Business Question:** How much total revenue did the company generate?

**Result:** 16,008,872.12 BRL

**Insight:** The business generated over **16 million BRL** in revenue during the observed period, providing a strong baseline for further sales and customer analysis.

## Query 2 – Total Orders

**Business Question:** How many orders were placed?

**Result:** 99,441 Orders

**Insight:** The platform processed nearly **100K orders**, indicating a large transactional dataset suitable for customer and sales analysis.

## Query 3 – Total Customers

**Business Question:** How many unique customers made purchases?

**Result:** 96,096 Customers

**Insight:** The customer base consists of over **96K unique customers**, showing that some customers placed multiple orders.

## Query 4 – Average Order Value

**Business Question:** What is the average amount spent per order?

**Result:** 160.99 

**Insight:** Average Order Value (AOV) measures how much customers typically spend per purchase and is an important retail performance metric.

## Query 5 – Revenue by State

**Business Question:** Which states generate the highest revenue?

**Top States**

| State | Revenue |
|-------|---------|
| SP |5998226.96|
| RJ |2144379.69|
| MG |1872257.26|
| RS |890898.54|
| PR |811156.38|

**Insight:** São Paulo generated the highest revenue, followed by Rio de Janeiro and Minas Gerais. These states represent the strongest markets for the business.

## Query 6 – Top Cities by Revenue

**Business Question:** Which cities contribute the most revenue?

**Result:** Sao Paulo, Rio de Janeiro, Belo horizonte, brasilia, curitiba, porto alegre, salvador, campinas, guarulhos, niteroi

**Insight:** Revenue is concentrated in a small number of large cities, highlighting major urban markets as key revenue drivers.

## Query 7 – Monthly Revenue

**Business Question:** How did revenue change over time?

**Result:** 
         Month          Revenue         
"2016-09-01 00:00:00"	252.24
"2016-10-01 00:00:00"	59090.48
"2016-12-01 00:00:00"	19.62
"2017-01-01 00:00:00"	138488.04
"2017-02-01 00:00:00"	291908.01
"2017-03-01 00:00:00"	449863.60
"2017-04-01 00:00:00"	417788.03
"2017-05-01 00:00:00"	592918.82
"2017-06-01 00:00:00"	511276.38
"2017-07-01 00:00:00"	592382.92
"2017-08-01 00:00:00"	674396.32
"2017-09-01 00:00:00"	727762.45
"2017-10-01 00:00:00"	779677.88
"2017-11-01 00:00:00"	1194882.80
"2017-12-01 00:00:00"	878401.48
"2018-01-01 00:00:00"	1115004.18
"2018-02-01 00:00:00"	992463.34
"2018-03-01 00:00:00"	1159652.12
"2018-04-01 00:00:00"	1160785.48
"2018-05-01 00:00:00"	1153982.15
"2018-06-01 00:00:00"	1023880.50
"2018-07-01 00:00:00"	1066540.75
"2018-08-01 00:00:00"	1022425.32
"2018-09-01 00:00:00"	4439.54
"2018-10-01 00:00:00"	589.67

**Insight:** Monthly revenue trends help identify business growth, seasonal demand, and changes in customer purchasing behavior.

## Query 8 – Monthly Orders

**Business Question:** How did order volume change over time?

**Result:** 
     Month              Total Orders
"2016-09-01 00:00:00"	4
"2016-10-01 00:00:00"	324
"2016-12-01 00:00:00"	1
"2017-01-01 00:00:00"	800
"2017-02-01 00:00:00"	1780
"2017-03-01 00:00:00"	2682
"2017-04-01 00:00:00"	2404
"2017-05-01 00:00:00"	3700
"2017-06-01 00:00:00"	3245
"2017-07-01 00:00:00"	4026
"2017-08-01 00:00:00"	4331
"2017-09-01 00:00:00"	4285
"2017-10-01 00:00:00"	4631
"2017-11-01 00:00:00"	7544
"2017-12-01 00:00:00"	5673
"2018-01-01 00:00:00"	7269
"2018-02-01 00:00:00"	6728
"2018-03-01 00:00:00"	7211
"2018-04-01 00:00:00"	6939
"2018-05-01 00:00:00"	6873
"2018-06-01 00:00:00"	6167
"2018-07-01 00:00:00"	6292
"2018-08-01 00:00:00"	6512
"2018-09-01 00:00:00"	16
"2018-10-01 00:00:00"	4

**Insight:** Order volume generally follows revenue trends and provides additional context for business performance over time.

## Query 9 – Revenue by Payment Method

**Business Question:** Which payment methods generated the most revenue?

**Result:** Credit Card.

**Insight:** Credit cards account for the largest share of transactions, making them the dominant payment method in the dataset.

## Query 10 – Order Status Distribution

**Business Question:** What is the distribution of order statuses?

**Result:** Most Orders were succesfully delivered.

**Insight:** Most orders were successfully delivered, while cancelled and unavailable orders represent only a small percentage of total transactions.