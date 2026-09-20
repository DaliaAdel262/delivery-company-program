# Delivery Trips Planner

A simple Python program that takes a list of package deliveries and organizes them into vehicle trips, following these rules:
- A vehicle can carry a maximum of 10kg per trip.
- Urgent deliveries (lower priority number) are handled first.
- Deliveries going to the same area are grouped into the same trip where reasonably possible.

## Folder Structure

- `main.py` — the entry point; runs the whole program from start to finish.
- `loader.py` — reads `sample.csv` and prepares the delivery data.
- `Trip.py` — defines what a "trip" is and what it can do (check space, add a package).
- `trips_planner.py` — the core logic that sorts deliveries and assigns them to trips.
- `exporter.py` — writes the final results out to CSV files.
- `sample.csv` — the input file you provide, listing all deliveries.
- `packages.csv` — *(generated)* every package and which trip it was assigned to.
- `trips.csv` — *(generated)* a summary of each trip (area, total weight, package count).
- `.gitignore` — tells git to ignore auto-generated files like `__pycache__`.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Put your delivery data in a file called `sample.csv`, in the same folder as the code. 

`sample.csv` should look like this:
id,area,priority,weight_kg
1,Nasr City,2,4.5
2,Maadi,1,2.0
3,Nasr City,3,1.2

3. Open a terminal in that folder and run:

```
   python main.py
```

4. The program will create two new files in the same folder:
   - `packages.csv` — every package, with the trip it was assigned to.
   - `trips.csv` — a summary of each trip (area, total weight, number of packages).

## My Approach

The program works in two simple steps:

1. **Sort the deliveries first** — by priority (most urgent first), then by area (so deliveries to the same place end up in same trip), then by weight (heaviest first, so big packages get placed before small ones fill up all empty vehicles).
2. **Place each delivery into a trip** — for each delivery, the program looks for an already-started trip going to the same area that still has room. If it finds one, it puts the delivery there. If not, it starts a new trip.

At the end, any package heavier than 10kg is set aside and reported separately, since no vehicle can carry it alone.

## What Was the Most Difficult Part?

Deciding which rule should be prioritized when the rules conflicted. For example: should the program prioritize handling urgent deliveries first, or grouping deliveries by area first? I chose to prioritize urgency first to ensure customer satisfaction (important in real world scenario) and use area as a secondary grouping rule to ensure faster delivery."

## Are There Cases Where the Grouping Isn't Perfect?

Yes. If there are several heavy packages in the same area that don't fit together in one trip, and there's no other package left over that can share the leftover space, each one ends up alone in its own trip, so it can end up using more trips than strictly necessary.

## What Would Slow Down at 1,000,000 Deliveries?

The part of the code that looks for a matching trip goes through every currently open trip for each new delivery. With a huge number of deliveries, this nested loop would get slower and slower as more trips get created, since each new delivery has to be compared against all the trips made so far.

## What Would I Improve With More Time?

Two things:
1. Speed up the matching step above, so it doesn't have to check every open trip one by one. Maybe find a way to store remaining space for each trip so it can look it up in O(1) instead of going through all trips everytime.
2. Add a cleanup step that looks for trips with extra room and tries to combine them with other trips — even from different areas — to reduce the total number of trips.

## Extra Feature: Exporting to CSV

I chose to export the results as two simple CSV files instead of just printing them to the screen, because that's closer to what a real delivery company would actually use. `packages.csv` and `trips.csv` can be opened directly in Excel or Google Sheets, sorted, filtered, or shared with a dispatch team — which is far more useful in practice than a one-time printout in a terminal window.