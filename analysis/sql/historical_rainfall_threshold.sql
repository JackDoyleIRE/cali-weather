WITH
historical_data AS (
  SELECT
    value as rainfall_inches
  FROM
    `cali_weather.station_rainfall`
  WHERE
    EXTRACT(YEAR FROM obsDate) < 2023
)
SELECT
  APPROX_QUANTILES(rainfall_inches, 100)[OFFSET(95)] as heavy_rainfall_threshold_inches
FROM
  historical_data