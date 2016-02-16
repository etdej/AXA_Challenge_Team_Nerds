class _Config:
    def __init__(self):
        # All samples
        self.useful_columns = ['DATE', 'DAY_OFF', 'DAY_DS', 'WEEK_END', 'DAY_WE_DS', 'ASS_ASSIGNMENT', 'CSPL_CALLS']
        self.months = { 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        self.days = {1: "MONDAY", 2: "TUESDAY", 3: "WEDNESDAY", 4: "THURSDAY", 5: 'FRIDAY', 6: "SATURDAY", 0: "SUNDAY"}
        self.ass_assign = ['A DEFINIR', 'Crises', 'DOMISERVE', 'Domicile', 'Gestion', 'Gestion - Accueil Telephonique', 'Gestion Amex', 'Gestion Assurances', 'Gestion Clients', 'Gestion Renault', 'Japon', 'LifeStyle', 'Manager', 'Maroc - G\xc3\xa9n\xc3\xa9riques', 'Medicine', 'M\xc3\xa9dical', 'NL Technique', 'Nuit', 'RENAULT', 'Regulation Medicale', 'R\xc3\xa9ception', 'SAP', 'Services', 'TAI - CARTES', 'TAI - PNEUMATIQUES', 'TAI - RISQUE', 'TAI - RISQUE SERVICES', 'TAI - SERVICE', 'TPA', 'Tech. Axa', 'Tech. Inter', 'Technical', 'Technique Belgique', 'Technique International', 'Truck Assistance', 'T\xc3\xa9l\xc3\xa9phonie', 'Tech. Total', 'NL M\xc3\xa9dical', 'Maroc - Renault', 'M\xc3\xa9canicien', 'Divers']

        self.default_columns = self.days.values()+self.months.values()+['TIME']+self.ass_assign+['CSPL_CALLS']
CONFIG = _Config()

print(len(CONFIG.default_columns))
print(len(CONFIG.ass_assign))