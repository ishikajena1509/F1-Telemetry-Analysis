# Formula 1 Telemetry Analysis
## ABOUT THIS PROJECT
This project analyzes real Formula 1 telemetry data to understand driver performance, compare racing strategies, and visualize race data using Python.

## TECHNOLOGIES USED
- Python
- FastF1
- Pandas
- NumPy
- Matplotlib

-----------------------------------------------------

## 📅 Day 1 – Project Setup

- Set up the Formula 1 Telemetry Analysis project.
- Installed Python libraries including FastF1, Pandas, and Matplotlib.
- Configured Jupyter Notebook and FastF1 cache.
- Loaded the first Formula 1 session successfully.
- Learned the project structure and workflow.

-----------------------------------------------------

## 📅 Day 2 – Exploring Session Data

- Loaded the **2026 Chinese Grand Prix Qualifying** session using FastF1.
- Explored session results and driver information.
- Retrieved driver names, team names, and qualifying times.
- Learned how to work with Pandas DataFrames.
- Practiced selecting columns and filtering Formula 1 data.

-----------------------------------------------------

## 📅 Day 3 – Driver and Lap Analysis

- Explored lap-by-lap telemetry data.
- Filtered laps for individual drivers using `pick_driver()`.
- Retrieved each driver's fastest lap using `pick_fastest()`.
- Learned the difference between a Pandas DataFrame and a Series.
- Understood how engineers isolate and analyze a driver's performance.

-----------------------------------------------------

## 📅 Day 4 – First Telemetry Visualization

- Extracted telemetry data using `get_car_data()`.
- Added lap distance using `add_distance()`.
- Created the first **Speed vs Distance** telemetry graph.
- Learned how to interpret braking zones, straights, and corner exits.
- Explored telemetry channels such as Speed, RPM, Throttle, Brake, Gear, and Distance.

-----------------------------------------------------

## 📅 Day 5 – Mercedes Teammate Comparison

- Compared Kimi Antonelli and George Russell's fastest qualifying laps.
- Created **Speed vs Distance**, **Throttle vs Distance**, and **Brake vs Distance** telemetry graphs.
- Compared lap times, top speeds, and minimum speeds.
- Analyzed how throttle application and braking behaviour influenced lap performance.
- Wrote an engineering-style telemetry report based on data analysis.

-----------------------------------------------------

## 📅 Day 6 – Sector & Delta Time Analysis

- Russell was marginally faster in Sector 1 by **0.001 s**.
- Antonelli gained **0.119 s** in Sector 2.
- Antonelli gained another **0.104 s** in Sector 3.
- Antonelli's final lap was **0.222 s** quicker overall.
- The lap advantage came from consistent gains in the middle and final sectors rather than one decisive corner.

-----------------------------------------------------

## 📅 Day 7 – RPM & Gear Analysis

- Compared RPM traces between Antonelli and Russell.
- Compared gear selection throughout the lap.
- Observed similar engine and gearbox behavior for both drivers.
- Connected RPM changes with gear shifts and acceleration.

-----------------------------------------------------

## 📅 Day 8 – DRS & Acceleration Analysis

- Compared DRS usage between Antonelli and Russell.
- Verified similar DRS activation patterns.
- Analyzed the relationship between DRS and top speed.
- Studied acceleration zones throughout the lap.
- Reinforced that better corner exits can outweigh higher top speed.

-----------------------------------------------------

## 📅 Day 9 – Braking Performance Analysis

- Compared brake traces between teammates.
- Calculated acceleration/deceleration from speed data.
- Identified major braking zones.
- Compared braking efficiency through telemetry.

-----------------------------------------------------

## 📅 Day 10 – Corner Performance Analysis

- Compared three representative corners.
- Evaluated throttle application after the apex.
- Identified stronger and weaker corners for each driver.
- Built an engineering summary of corner performance.

-----------------------------------------------------