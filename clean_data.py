import pandas as pd

athlete = pd.read_excel("Athletes.xlsx")
medals = pd.read_excel("Medals.xlsx")

medals = medals.drop("Total", axis = 1)

# medals_2
medals_2 = pd.melt(medals, id_vars = ["Rank", "Country", "Rank by Total"], value_vars = ["Gold", "Silver", "Bronze"], var_name = "Medal Type", value_name = "Total")
# medals_2.to_excel("Medals_2.xlsx", index = False)

# Athletes
athlete = athlete.drop("Discipline", axis = 1)
athlete = athlete.groupby("NOC", as_index = False).count()
# athlete.to_excel("Athlete_2.xlsx", index = False)

# Covid
covid = pd.read_excel("Covid.xlsx")
covid = covid.drop("Total", axis = 1)
covid = pd.melt(covid, id_vars = "Date", value_vars = ["Athlete", "Games-concerned personnel", "Media", "Employee", "Contractor", "Volunteer", "Spectator"], var_name = "Personnel", value_name = "Total")
definition = pd.read_excel("Personnel Definition.xlsx")
covid = pd.merge(covid, definition, on = "Personnel", how = "left")
# print(covid)
# covid.to_excel("Covid_2.xlsx", index = False)

# Gender
gender = pd.read_excel("EntriesGender.xlsx")
gender = gender.drop("Total", axis = 1)
gender = pd.melt(gender, id_vars = "Discipline", value_vars = ["Female", "Male"], var_name = "Gender", value_name = "Total")
gender.to_excel("Gender_2.xlsx", index = False)


