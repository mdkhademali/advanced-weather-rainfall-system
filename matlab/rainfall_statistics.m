
data = readtable('../data/raw/weather_timeseries.csv');

rain = data.rainfall_mm;

mean_rain = mean(rain);
median_rain = median(rain);
std_rain = std(rain);

disp("Rainfall Statistics")
disp(mean_rain)
disp(median_rain)
disp(std_rain)

figure
plot(rain)
title('Rainfall Time Series')
xlabel('Day')
ylabel('Rainfall mm')
