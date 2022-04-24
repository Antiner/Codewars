"""I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]"""


def human_years_cat_years_dog_years(human_years: int):
    cat_years = 0
    dog_years = 0
    for i in range(1, human_years + 1):
        if i == 1:
            cat_years += 15
            dog_years += 15
        elif i == 2:
            cat_years += 9
            dog_years += 9
        else:
            cat_years += 4
            dog_years += 5
    return [human_years, cat_years, dog_years]


"""Best practice"""


def human_years_cat_years_dog_years(x):
    return [x, 24 + (x - 2) * 4 if (x != 1) else 15, 24 + (x - 2) * 5 if (x != 1) else 15]
