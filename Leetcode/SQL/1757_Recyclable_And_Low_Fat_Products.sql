# 1757. Recyclable and Low Fat Products
# https://leetcode.com/problems/recyclable-and-low-fat-products/
# Write an SQL query to find the ids of products that are both low fat and recyclable.
# product_id is the primary key for this table.
# low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
# recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
select product_id
from Products
where low_fats = "Y" and recyclable = "Y"