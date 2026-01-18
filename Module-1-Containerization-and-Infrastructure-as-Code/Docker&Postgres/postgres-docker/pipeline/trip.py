import pandas as pd

# Step 1: Load both datasets
print("Loading data...")
trips_df = pd.read_parquet('green_tripdata_2025-11.parquet')
zones_df = pd.read_csv('taxi_zone_lookup.csv')

print(f"Trips data shape: {trips_df.shape}")
print(f"Zones data shape: {zones_df.shape}")

# Step 2: Filter for November 2025 (pickup between Nov 1 and Dec 1, exclusive)
nov_trips = trips_df[
    (trips_df['lpep_pickup_datetime'] >= '2025-11-01') & 
    (trips_df['lpep_pickup_datetime'] < '2025-12-01')
].copy()
print(f"\nTrips in November 2025: {len(nov_trips):,}")

# Step 3: Merge pickup zones to filter for "East Harlem North"
# First, get the LocationID for "East Harlem North"
east_harlem_north_id = zones_df[zones_df['Zone'] == 'East Harlem North']['LocationID'].values[0]
print(f"\nLocationID for 'East Harlem North': {east_harlem_north_id}")

# Step 4: Filter trips that started in East Harlem North
ehn_pickups = nov_trips[nov_trips['PULocationID'] == east_harlem_north_id].copy()
print(f"Trips picked up in East Harlem North: {len(ehn_pickups):,}")

# Step 5: Merge with zones data for drop-off zone names
# We need to merge on DOLocationID (drop-off location ID)
merged_df = pd.merge(
    ehn_pickups,
    zones_df[['LocationID', 'Zone']],
    left_on='DOLocationID',
    right_on='LocationID',
    how='left',
    suffixes=('', '_dropoff')
)

# Rename the zone column to be clear it's drop-off zone
merged_df = merged_df.rename(columns={'Zone': 'dropoff_zone'})

# Step 6: Group by drop-off zone and find the one with maximum tip
# First, let's find the maximum tip amount per drop-off zone
dropoff_tips = merged_df.groupby('dropoff_zone')['tip_amount'].max().reset_index()

# Sort by tip_amount in descending order
dropoff_tips = dropoff_tips.sort_values('tip_amount', ascending=False)

print("\n" + "="*60)
print("TOP 10 DROP-OFF ZONES BY MAXIMUM TIP AMOUNT:")
print("="*60)
print(dropoff_tips.head(10))

# Step 7: Filter for only the zones in the question
target_zones = ['JFK Airport', 'Yorkville West', 'East Harlem North', 'LaGuardia Airport']

target_zone_tips = dropoff_tips[dropoff_tips['dropoff_zone'].isin(target_zones)]

print("\n" + "="*60)
print("SPECIFIC ZONES FROM THE LIST:")
print("="*60)
print(target_zone_tips)

# Step 8: Get the answer
if not target_zone_tips.empty:
    top_zone = target_zone_tips.iloc[0]
    print(f"\n" + "="*60)
    print(f"ANSWER: The drop-off zone with the largest tip is:")
    print(f"'{top_zone['dropoff_zone']}' with tip amount: ${top_zone['tip_amount']:.2f}")
    print("="*60)
else:
    print("\nNone of the specified drop-off zones were found in the data")