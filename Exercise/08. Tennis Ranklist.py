from math import floor

tournaments = int(input())
points = int(input())
wins = int()
points_season = int()

for i in range(0, tournaments):
    finish = input()

    if finish == 'W':
        points_season += 2000
        wins += 1
    elif finish == 'F':
        points_season += 1200
    elif finish == 'SF':
        points_season += 720

total_points = points + points_season
average_points = floor(points_season / tournaments)
percentage_wins = (wins / tournaments) * 100

print(f"Final points: {total_points}\n"
      f"Average points: {average_points}\n"
      f"{percentage_wins:.2f}%")
