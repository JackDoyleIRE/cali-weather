SELECT
  *
FROM
  `tranquil-gasket-374723.cali_weather.rainfall_data` rainfall
LEFT JOIN
  `cali_weather.weather_stations` stations
ON
  rainfall.stationId = stations.id