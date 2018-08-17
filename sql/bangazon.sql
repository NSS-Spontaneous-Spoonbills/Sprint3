-- Sql Scripts to assist with faker data so that some content makes relevant sense
-- Author: Jacob Smith

-- CUSTOMERS

INSERT INTO Customer VALUES (null, '2017-08-17','2018-07-25', 'Jacob', 'Smith', '1234 Cool Blvd', 'Nashville', 'TN', 37210, 'jacob_andrew', 4444444444)
INSERT INTO Customer VALUES (null, '2018-03-08','2017-06-25', 'Donkey', 'Kong', '2442 Oakley St', 'Dallas', 'TX', 90210, 'DKong55', 5555555555)
INSERT INTO Customer VALUES (null, '2017-09-09','2018-08-16', 'Michelle', 'Obama', '88993 Spence Ln', 'San Francisco', 'CA', 23210, 'michelleOB', 1111111111)
INSERT INTO Customer VALUES (null, '2017-10-01','2018-04-01', 'Grace', 'Hopper ', '443235 LaMirada St', 'Portland', 'OR', 98765, 'Grace-XBugs', 2222222222)
INSERT INTO Customer VALUES (null, '2018-02-17','2018-08-17', 'Jacob', 'Smith', '1234 Cool Blvd', 'Nashville', 'TN', 37210, 'jacob_andrew', 8888888888)


-- PRODUCT TYPES

INSERT INTO Product_Type VALUES (null, 'Hiking')
INSERT INTO Product_Type VALUES (null, 'Electronics')
INSERT INTO Product_Type VALUES (null, 'Books')
INSERT INTO Product_Type VALUES (null, 'Automotive')
INSERT INTO Product_Type VALUES (null, 'Beauty & Health')
INSERT INTO Product_Type VALUES (null, 'Kitchen')
INSERT INTO Product_Type VALUES (null, 'Sports')
INSERT INTO Product_Type VALUES (null, 'Handmade')
INSERT INTO Product_Type VALUES (null, 'Pet')
INSERT INTO Product_Type VALUES (null, 'Home Services')
INSERT INTO Product_Type VALUES (null, 'Music')

-- PAYMENT TYPES

INSERT INTO Payment_Type_Name VALUES (null, 'Visa')
INSERT INTO Payment_Type_Name VALUES (null, 'Mastercard')
INSERT INTO Payment_Type_Name VALUES (null, 'Discover')
INSERT INTO Payment_Type_Name VALUES (null, 'Venmo')
INSERT INTO Payment_Type_Name VALUES (null, 'Paypal')


