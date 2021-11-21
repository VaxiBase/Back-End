class Province:

    def __init__(self, name, date, percent_vaccinated_total):
        self.name = name
        self.date = date
        self.percent_vaccinated_total = percent_vaccinated_total

    def __str__(self):
        return  f'Province(name={self.name}, updated={self.date}, total % vaccinated={self.percent_vaccinated_total})'