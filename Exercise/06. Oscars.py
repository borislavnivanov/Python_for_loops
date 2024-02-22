actor_name = input()
academy_points = float(input())
number_of_judges = int(input())

for i in range(0, number_of_judges):

    points = 0.00
    judge_name = input()
    awarded_points = float(input())
    points += (len(judge_name) * awarded_points) / 2
    academy_points += points

    if academy_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        break

if academy_points < 1250.5:
    print(f'Sorry, {actor_name} you need {abs(academy_points - 1250.5):.1f} more!')
