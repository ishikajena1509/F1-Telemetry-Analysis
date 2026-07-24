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

# China GP 2026 Qualifying - Mercedes Teammate Analysis

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