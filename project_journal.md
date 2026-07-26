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

# China GP 2026 Qualifying – RPM & Gear Analysis-DAY 7

## Drivers
- Kimi Antonelli
- George Russell

## Objective
Compare engine RPM and gear selection between the fastest qualifying laps to understand engine behavior and shifting strategy.

## RPM Analysis

### Observations
- Both drivers displayed very similar RPM traces throughout the lap.
- RPM increased steadily during acceleration and dropped after each upshift.
- The highest RPM values were observed on the main straights before gear changes.
- The lowest RPM values occurred during heavy braking and slow-speed corners.

## Gear Analysis

### Observations
- Both drivers used the complete gear range available during the lap.
- Gear changes followed nearly identical patterns, indicating similar racing lines and shift strategies.
- Downshifts occurred before corner entry, while upshifts followed acceleration on corner exit and long straights.

## Engineering Interpretation

The close similarity in RPM and gear traces indicates that both Mercedes drivers operated the car in a very similar manner. Engine RPM closely followed gear selection, demonstrating efficient acceleration and braking phases. Small differences in lap time are therefore more likely to result from corner execution and throttle application rather than gearbox strategy.

## Conclusion

RPM and gear telemetry provide valuable insight into how a driver extracts performance from the car. When combined with speed, throttle, brake, sector, and delta time analysis, these telemetry channels help engineers identify subtle performance differences that are not apparent from lap times alone.

# China GP 2026 Qualifying – DRS & Acceleration Analysis-DAY 8

## Drivers
- Kimi Antonelli
- George Russell

## Objective
Analyze DRS usage and acceleration characteristics to understand their influence on qualifying lap performance.

## DRS Analysis

### Observations
- Both drivers activated DRS in the designated activation zones.
- DRS usage patterns were nearly identical throughout the lap.
- DRS remained closed during cornering sections to maintain aerodynamic stability.
- Maximum speeds were achieved while DRS was active on the straights.

## Speed & Acceleration Analysis

### Observations
- Speed increased rapidly after corner exits as throttle application reached maximum.
- Russell achieved the highest top speed during the lap.
- Antonelli maintained stronger average pace through technical sections despite a slightly lower top speed.
- Corner exits had a greater influence on overall lap time than maximum straight-line speed.

## Engineering Interpretation

The telemetry indicates that both drivers used DRS efficiently and consistently. Since DRS usage was almost identical, the lap time difference cannot be attributed solely to aerodynamic assistance. Instead, Antonelli's superior corner exits and smoother acceleration through technical sections enabled him to build a cumulative time advantage despite Russell achieving the higher maximum speed.

## Conclusion

DRS provides a valuable speed advantage on straights, but overall lap performance depends on the combination of corner exit speed, throttle application, acceleration, and driver consistency. Telemetry analysis confirms that maintaining momentum through multiple corners is often more important than achieving the highest top speed.

# China GP 2026 Qualifying – Braking Performance Analysis-DAY 9

## Drivers
- Kimi Antonelli
- George Russell

## Objective
Analyze braking performance, deceleration, and braking zones to compare the driving techniques of both Mercedes drivers during qualifying.

## Brake Telemetry Analysis

### Observations
- Both drivers braked at nearly identical locations around the circuit.
- Brake application corresponded closely with major corner entry points.
- Long straight sections showed no brake application.
- Brake traces indicated consistent braking strategies between teammates.

## Deceleration Analysis

### Observations
- Acceleration was calculated from changes in speed over time.
- Negative acceleration values represented braking events.
- The strongest negative peaks corresponded to heavy braking zones.
- Both drivers produced similar deceleration profiles throughout the lap.

## Braking Zone Comparison

### Observations
- Major braking events occurred before slow and medium-speed corners.
- Speed reduced rapidly after brake application.
- Smooth transition from braking to acceleration was visible after each corner.
- Efficient braking contributed to maintaining momentum through technical sections.

## Engineering Interpretation

Although both drivers used similar braking points, overall lap performance depended on how efficiently they transitioned from braking into cornering and then back to acceleration. The telemetry suggests that consistency in braking and smooth corner entry are just as important as braking as late as possible.

## Conclusion

Braking performance is not determined solely by the braking point. The combination of controlled deceleration, balanced corner entry, and strong acceleration on corner exit plays a crucial role in producing a competitive qualifying lap.

# China GP 2026 Qualifying – Corner Performance Analysis-DAY 10

## Drivers
- Kimi Antonelli
- George Russell

## Objective
Analyze corner entry, apex speed, throttle application, and corner exit performance to determine where lap time was gained and lost.

## Corner Entry Analysis
### Observations
- Both drivers followed similar braking points.
- Speed reduced consistently before each major corner.
- Small differences appeared in minimum corner speed.

## Apex Analysis
### Observations
- Apex speed varied slightly between drivers.
- Maintaining a higher minimum speed helped preserve momentum.
- Small differences at the apex influenced corner exit performance.


## Corner Exit Analysis
### Observations
- Throttle traces showed how quickly each driver accelerated after the apex.
- Earlier throttle application resulted in stronger acceleration onto the following straight.
- Smooth throttle application improved overall stability and momentum.

## Corner Comparison

| Corner | Stronger Driver | Reason |
|---------|-----------------|--------|
| Corner 1 | (Your Observation) | Earlier throttle / Higher minimum speed |
| Corner 2 | (Your Observation) | Better corner exit |
| Corner 3 | (Your Observation) | Smoother acceleration |

## Engineering Interpretation

The telemetry demonstrates that overall lap time is influenced more by efficient corner exits than by isolated top-speed advantages. Drivers who return to full throttle earlier build a speed advantage that continues throughout the following straight. Consistency across multiple corners ultimately determines the fastest qualifying lap.

## Key Findings

- Corner exits had a greater impact than top speed.
- Earlier throttle application improved acceleration.
- Small differences at the apex accumulated into measurable lap-time gains.
- Telemetry analysis identified specific corners where performance differed between teammates.

## Conclusion

Corner performance is a combination of braking, apex speed, and throttle application. A driver who balances these three phases effectively is more likely to produce a consistently faster lap than one relying solely on late braking or maximum straight-line speed.

# China GP 2026 Qualifying – Professional Telemetry Dashboard-DAY 11

## Drivers
- Kimi Antonelli
- George Russell

## Objective
Develop a professional multi-channel telemetry dashboard to compare driver performance using synchronized telemetry data.

## Dashboard Channels

- Speed
- Throttle
- Brake
- Gear
- RPM
- DRS

## Key Observations
### Speed
Both drivers reached competitive top speeds, but differences appeared mainly during corner entry and exit.

### Driver Inputs
Throttle and brake traces revealed how each driver managed acceleration and deceleration throughout the lap.

### Gear & RPM
Gear shifts and RPM changes closely followed acceleration and braking events, showing the relationship between engine performance and driver inputs.

### DRS
Both drivers activated DRS in the permitted zones, indicating similar aerodynamic assistance during qualifying.

## Engineering Interpretation

Viewing multiple telemetry channels together provided a much clearer understanding of driver performance than analyzing individual plots separately. Correlating speed, throttle, brake, gear, RPM, and DRS allowed identification of the reasons behind differences in lap performance rather than simply observing the final lap time.

## Conclusion

A multi-channel telemetry dashboard is an effective engineering tool for understanding driver behavior, vehicle response, and overall lap performance.

# Day 12 – Interactive Dashboard
## Topics Learned
- Plotly
- Interactive visualizations
- Subplots
- HTML dashboard export

## Completed
- Built interactive telemetry dashboard
- Added synchronized telemetry plots
- Exported dashboard as HTML

## Biggest Learning
Interactive dashboards allow engineers to inspect telemetry dynamically by zooming, hovering, and comparing multiple drivers in real time.

## Conclusion
Interactive dashboards provide a more engaging way to analyze telemetry data than static plots and improve the usability of the project for demonstrations and portfolio presentations.

# Day 13 – Dashboard Enhancement
## Objective

Improve the Formula 1 telemetry dashboard by adding performance summaries and professional visualization.

## Features Added

- Improved dashboard styling
- Driver performance summary
- KPI comparison table
- Interactive HTML export

## Skills Learned

- Plotly tables
- Dashboard KPIs
- Performance metrics
- Data summarization

## Engineering Takeaways

- Summary statistics provide a quick overview before detailed telemetry analysis.
- Interactive dashboards improve the analysis workflow.
- Combining visualization with statistics creates a more complete engineering report.

# Day 14 – Streamlit Dashboard
## Objective
Transform the Formula 1 telemetry analysis into an interactive web application using Streamlit.

## Features Implemented

- Interactive Streamlit dashboard
- Driver selection using sidebar
- Speed comparison using Plotly
- Driver performance summary
  - Top Speed
  - Average Speed
  - Maximum RPM
- Engineering Insights section
- About section

## Technologies Used

- Python
- FastF1
- Plotly
- Streamlit
- Pandas

## Challenges Faced

- Streamlit installation and PATH configuration
- Cache directory issue
- Integrating Plotly with Streamlit
- Organizing dashboard layout

## Conclusion

Successfully built an interactive Formula 1 telemetry dashboard capable of comparing two drivers with live visualizations and performance statistics.