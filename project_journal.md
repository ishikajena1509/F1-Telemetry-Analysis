## Day 1
### Goal
Set up the project environment and understand the project objective.

### Completed
- Installed Python
- Installed VS Code extensions
- Installed required libraries
- Created project structure

### Learned
- FastF1 session structure
- Car telemetry
- Distance-based plotting
- Jupyter notebooks
- FastF1 caching

### Conclusion
Successfully built my first F1 telemetry visualization.

## Day 2
### Topics Learned
- head()
- columns
- info()
- describe()
- Selecting columns
- Sorting
- Filtering

### Key Observations
- China 2026 has 22 drivers.
- Q1 has data for all drivers.
- Q2 contains only drivers who advanced.
- Q3 contains only the top 10 qualifiers.

### Biggest Learning
Understanding the structure of a dataset is the first step before analysis.

## Day 3
### Topics Learned
- describe()
- Selecting columns
- Sorting data
- Boolean filtering
- Creating a custom DataFrame

### Key Observations
- Q1 includes all 22 drivers.
- Q2 includes only the top 16.
- Q3 includes only the top 10.
- Smaller DataFrames make analysis easier.

### Biggest Learning
A DataFrame can be customized to contain only the information needed for a specific analysis.

## Day 4
### Topics Learned
- session.laps
- pick_driver()
- pick_fastest()
- get_car_data()
- add_distance()
- Speed vs Distance plot

### Key Takeaways
- A session can be analyzed at different levels: results, laps, and telemetry.
- Telemetry provides thousands of data points for a single lap.
- Distance is preferred over time when comparing drivers because it aligns data to positions on the track.
- Speed traces reveal braking zones, straights, and corner exits.

# China GP 2026 Qualifying - Mercedes Teammate Analysis-DAY 5

## Drivers
- Kimi Antonelli
- George Russell

## Objective
Compare the fastest qualifying laps using telemetry.

## Lap Time Comparison
- Antonelli:1:32.064
- Russell:1:32.286
- Faster Driver:Kimi Antonelli

## Speed Analysis
- Antonelli Top Speed:332 km/hr
- Russell Top Speed:333 kmm/hr
- Driver with Higher Top Speed:George Russel

## Telemetry Observations
- Antonelli completed the faster qualifying lap despite having a slightly lower top speed.
- Russell reached the highest top speed (333 km/h), while Antonelli reached 332 km/h, showing that straight-line speed alone did not determine the faster lap.
- Both drivers recorded the same minimum speed of 68 km/h, indicating similar performance through the slowest corner.
- Both drivers achieved their maximum speed at approximately 4.0 km into the lap, suggesting they reached top speed on the same long straight.
- The speed traces were very similar throughout the lap, but Antonelli carried slightly more speed through several corner exits.
- The throttle comparison showed Antonelli generally returned to full throttle slightly earlier after some corners, helping improve acceleration.
- The brake traces indicated both drivers used very similar braking points, with only minor differences in brake application timing.


## Conclusion
Telemetry comparison suggests that the lap time difference was mainly influenced by Kimi rather than Russel.Although George Russell achieved the higher top speed of 333 km/h, Kimi Antonelli completed the faster lap with a time of 1:32.064, which was 0.222 seconds quicker than Russell. The telemetry suggests that the lap time advantage came from more efficient corner exits and earlier throttle application rather than higher straight-line speed. Since both drivers had nearly identical braking points and the same minimum speed, Antonelli's smoother acceleration out of corners was likely the key factor in producing the quicker qualifying lap.

# China GP 2026 Qualifying – Sector & Delta Time Analysis-DAY 6

## Drivers
- Kimi Antonelli
- George Russell

## Objective
Compare sector performance and delta time between the fastest qualifying laps to determine where lap time was gained or lost.

## Sector Analysis

### Sector 1
- Faster Driver:George Russel
- Time Difference:0.001s

### Sector 2
- Faster Driver:Kimi Antonelli
- Time Difference:0.119s

### Sector 3
- Faster Driver:Kimi Antonelli
- Time Difference:0.104s

## Delta Time Analysis

### Observations
-The delta remained almost unchanged through Sector 1, showing that both drivers had nearly identical pace at the beginning of the lap.
-The largest increase in Antonelli's advantage occurred during Sector 2, where he gained approximately 0.119 seconds over Russell.
-Antonelli extended his lead slightly further in Sector 3, gaining another 0.104 seconds.
-Russell's only advantage was a 0.001-second gain in Sector 1, which was too small to affect the overall result.
-The final lap time difference of 0.222 seconds was created by consistent gains across Sectors 2 and 3, rather than by a single dramatic moment.

## Engineering Interpretation

The sector analysis provides an overview of where the lap time difference occurred, while the delta time graph identifies the exact locations where performance changed.

The telemetry suggests that the final lap time difference was created through a combination of multiple small gains rather than a single corner.

## Conclusion

Delta time analysis provides a much more detailed understanding of driver performance than sector times alone. It allows engineers to pinpoint exactly where time is gained or lost and helps guide further investigation using telemetry channels such as speed, throttle, and brake data.