class Province:

    def __init__(self, name, date, percent_vaccinated_total, population_death,total_hospitalizations, booster_shots):
        self.name = name
        self.date = date
        self.percent_vaccinated_total = percent_vaccinated_total
        self.population_death = population_death
        self.total_hospitalizations = total_hospitalizations
        self.percent_booster_shot = booster_shots


    def __str__(self):
        return  f'Province(name={self.name}, updated={self.date}, total % vaccinated={self.percent_vaccinated_total},fatalities ={self.population_death}, total % boosterSHot={self.percent_booster_shot})'
