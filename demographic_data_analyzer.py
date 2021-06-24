import pandas as pd


def calculate_demographic_data(print_data=True):

    df = pd.read_csv("adult.data.csv")
    
    # print(df)
    # print(df.age)

    race_count = df["race"].value_counts()
    # print("race>>",race_count)

    average_age_men = df[df["sex"] == "Male"]["age"].mean().round(1)

    # num_of_bachelors = ([df["education"] == "Bachelors"]).size
    num_of_bachelors = len(df[df["education"] == "Bachelors"])
    total_education = df["education"].size

    percentage_bachelors = round(num_of_bachelors / total_education *100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # subset_df = df[(df["A"] >= 1) & (df["B"] < 5)]
    # bachelors = df[(df["education"] == "Bachelors")]
    # doctorates = df[(df["education"] == "Doctorate")]
    # masters = df[(df["education"] == "Masters")]



    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    
    # print("higher", len(higher_education),"lower",len((lower_education))

    # percentage with salary >50K
    non_percentage_higher = len(higher_education[higher_education.salary == ">50K"])

    # higher_education_rich = round(non_percentage_higher / (higher_education).size *100 , 1)

    higher_education_rich = round(non_percentage_higher / len(higher_education) *100 , 1)

    non_percentage_lower = len(lower_education[lower_education["salary"] == ">50K"])

    lower_education_rich = round(non_percentage_lower / len(lower_education) *100 , 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(len(num_min_workers[num_min_workers["salary"] == ">50K"]) / len(num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()