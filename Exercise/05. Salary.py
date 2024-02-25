FACEBOOK_PENALTY = 150
INSTAGRAM_PENALTY = 100
REDDIT_PENALTY = 50

browser_tabs = int(input())
salary = int(input())

for i in range(0, browser_tabs):
    website = input()
    if website == 'Facebook':
        salary -= FACEBOOK_PENALTY
    elif website == 'Instagram':
        salary -= INSTAGRAM_PENALTY
    elif website == 'Reddit':
        salary -= REDDIT_PENALTY

    if salary <= 0:
        print('You have lost your salary.')
        break

else:
    print(salary)
