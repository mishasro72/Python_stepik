
#dice = [1, 1, 1, 4, 1]

def score(dice):
    score = 0
    numbers = [0 for _ in range(6)]
    points = [1000, 200, 300, 400, 500, 600]
    ext_points = [100, 0, 0, 0, 50, 0]

    for die in dice:
        numbers[die - 1] += 1

    for i, count in enumerate(numbers):
        score += (points[i] if count >= 3 else 0) + ext_points[i] * (count%3)
    return score

#print(score(dice))
