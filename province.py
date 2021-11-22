class Province:

    def __init__(self, name, date, percent_vaccinated_total, total_vaccinations, total_vaccinated, total_cases, total_hospitalizations, total_fatalities):
        self.name = name
        self.date = date
        self.percent_vaccinated_total = percent_vaccinated_total
        self.total_vaccinations = total_vaccinations
        self.total_vaccinated = total_vaccinated
        self.total_cases = total_cases
        self.total_hospitalizations = total_hospitalizations
        self.total_fatalities = total_fatalities


    def __str__(self):
        return  f'Province(name={self.name}, date={self.date}, total % vaccinated={self.percent_vaccinated_total}, total vaccinations={self.total_vaccinations}, total vaccinated={self.total_vaccinated}, total cases-{self.total_cases}, total hospitalizations={self.total_hospitalizations}, total fatalities={self.total_fatalities})'