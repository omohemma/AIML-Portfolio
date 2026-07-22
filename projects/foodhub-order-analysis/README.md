# FoodHub Order Analysis

## Overview

Exploratory data analysis project for FoodHub, a food aggregator platform. The analysis studies customer orders, restaurant performance, cuisine demand, order costs, ratings, preparation time, and delivery time to identify business improvement opportunities.

## Business Problem

FoodHub wants to understand order behavior and restaurant performance so it can improve customer experience, delivery operations, and promotional strategy.

## Dataset

- File: `data/foodhub_order.csv`
- Rows: 1,898
- Columns: 9
- Key fields: cuisine type, order cost, rating, preparation time, delivery time, restaurant name
- Target variable: none; this is an EDA and business insights project

## Approach

- Loaded and inspected order-level data
- Checked missing values and disguised missing ratings
- Analyzed order costs, cuisine demand, restaurant popularity, ratings, food preparation time, and delivery time
- Compared weekday and weekend behavior
- Developed business recommendations from observed patterns

## Key Insights

- The dataset contains 1,898 orders from 178 restaurants.
- Total observed revenue is about 6,166.3 in the notebook's cost units.
- Most orders are below 20, showing strong demand for affordable meals.
- American cuisine appears as the most popular cuisine category.
- Rating collection needs improvement because many orders have ratings marked as `Not given`.

## Recommendations

- Encourage customers to leave ratings through small incentives or post-delivery prompts.
- Monitor long delivery orders and weekday delivery delays.
- Use cuisine and restaurant demand patterns to guide promotions.
- Create loyalty campaigns for frequent customers.

## Files

```text
foodhub-order-analysis/
  README.md
  notebooks/foodhub_order_analysis.ipynb
  data/foodhub_order.csv
  reports/foodhub_order_analysis.html
  assets/screenshots/
```
