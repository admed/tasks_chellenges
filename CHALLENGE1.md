

Diagram online

https://dbdiagram.io/d/612ccfd9825b5b0146ead3ac

### Questions and Answers

 *** 1) what you think this system would do ***

 System can be some sort of internal sales database tracking producs they sell, customers, and suppliers. I think it could help help sales representatives or managers at a small company selling widgets to create specially priced their customers. Their business driver could be to incentivize their Retailers to increase their purchase quantities and purchasing frequency. I think this system could be connected to Invoice system to track sales and incomes.
 
 
 *** 2) what you feel would be a reasonable database structure for the data and a reasonable architecture for the system ***

I created example database schema using dbdiagram

https://dbdiagram.io/d/612ccfd9825b5b0146ead3ac

Data looks like are mixed from different sources. I decided to create separate tables for Widgets (main table), Packages, Customers, Suppliers and Warehouse.

 *** 3) any questions or concerns you have regarding this dataset/system that might need to be answered before establishing an ideal database/solution for such a system. ***

I would like to know kind the purpose of creating the system and what are the business/user needs. 
In example there is just small portion of data. I would like to know how much of data system will contain.

Regarding the example data set, I would like to know:
What is the current data model or database? Are there any? 
What is the mining of qty and min qty. Are they connected to inventory, orders, or something else? Should be some restriction regading min_qty?
What represents the prices? Is it the amount that Customers have paid for Widget?
Should we store more data like dates, invoices etc? 
Should we connect the system to other databases? 