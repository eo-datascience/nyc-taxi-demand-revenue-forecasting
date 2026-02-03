# NYC Taxi Demand & Revenue Forecasting

## Overview

This project presents an end-to-end analytics and forecasting dashboard built with Power BI, designed to analyze historical NYC taxi trip data and generate short-term demand forecasts. The dashboard combines exploratory analysis, trend detection, behavioral patterns, and predictive modeling to support data-driven transportation and revenue insights.


## Objectives
- Analyze historical taxi demand and revenue trends
- Understand temporal patterns (daily, weekly, intra-month)
- Examine relationships between trip distance, fare, and duration
- Forecast future taxi demand using time-series modeling
- Present insights in a clean, executive-ready Power BI dashboard


## Data Description

The primary dataset contains daily aggregated NYC taxi metrics, including:
- Total trips
- Total revenue
- Average fare
- Average trip distance
- Average trip duration
- Trip date and derived calendar features (day, week, month)

A separate forecast table was created to store model-generated future demand values.


## Exploratory & Descriptive Analytics

The dashboard includes the following analytical components:

KPI Summary
- Total Trips
- Total Revenue
- Average Fare
- Average Trip Duration

Trend Analysis
- Daily trip volume trend
- Daily revenue trend

Demand Behavior Analysis
- Trips by day of week
- Intra-month daily demand patterns
- Distribution of trips by average duration
- Relationship between fare and trip distance (demand-weighted)

These views help identify seasonality, weekday vs weekend behavior, and demand concentration by trip characteristics.


## Forecasting Methodology

To extend the analysis beyond historical data, a time-series forecasting step was performed.

Forecast Model
- A forecasting model (trained outside Power BI) was used to predict future total trips
- Forecast horizons included short-term daily demand projections
- Forecasted values were imported into Power BI as a separate table
- A relationship was created between historical and forecast data using the trip date

Purpose of Forecasting
- Anticipate near-term taxi demand
- Support operational planning and revenue expectations
- Demonstrate applied predictive analytics alongside BI reporting

Note: Since actual values for future dates are unavailable, the forecast is presented as a standalone predictive output, not a model accuracy comparison.


## Dashboard Design Principles
- Minimal, controlled color palette for clarity and professionalism
- KPI cards prioritized for executive readability
- Clean grid layout with consistent spacing
- Subtle gridlines and muted axes to keep focus on trends
- Clear chart titles focused on what the user is seeing, not interpretations


## Tools & Technologies
- Power BI : data modeling, visualization, dashboard design
- Power Query (M) : data ingestion, cleaning, transformation, feature preparation
- Data Modeling : star-schema design, relationships, date handling
- DAX : calculated measures, aggregations, KPIs
- Python / ML (external) : time-series forecasting model development
- Time-series analysis : demand forecasting and trend modeling


## Key Takeaways
- Taxi demand shows consistent weekday patterns with intra-month fluctuations
- Revenue closely follows trip volume trends
- Most trips cluster around mid-range durations
- Forecasting provides a forward-looking extension to historical BI analysis

## Note on Data Availability

Some raw and intermediate data files used in this project exceed GitHub’s file size limits and are therefore not included in this repository. The project structure and analysis logic are fully preserved, and the code can be executed on the original datasets if they are available locally.

### Author

Built by Emmanuel Olusolade

Focus areas: Data Analytics, Business Intelligence, and Predictive Modeling



