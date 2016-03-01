class _Config:
    def __init__(self):
        # All samples
        self.useful_columns = ['DATE', 'DAY_OFF', 'DAY_WE_DS', 'WEEK_END', 'ASS_ASSIGNMENT', 'CSPL_CALLS', 'CSPL_RECEIVED_CALLS']
        self.months = { 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        self.days = {1: "MONDAY", 2: "TUESDAY", 3: "WEDNESDAY", 4: "THURSDAY", 5: 'FRIDAY', 6: "SATURDAY", 0: "SUNDAY"}
        self.ass_assign = {'A DEFINIR': 0, 'AEVA': 41, 'CAT': 43,'CMS': 46, 'Crises': 1,'DOMISERVE': 2,'Divers': 40, 'Domicile': 3, 'Evenements': 53, 'FO Remboursement': 44, 'Finances PCX': 48,'Gestion': 4, 'Gestion - Accueil Telephonique': 5, 'Gestion Amex': 6, 'Gestion Assurances': 7, 'Gestion Clients': 8, 'Gestion DZ': 45, 'Gestion Relation Clienteles': 42, 'Gestion Renault': 9, 'IPA Belgique - E/A MAJ': 52, 'Japon': 10, 'Juridique': 54, 'KPT': 47, 'LifeStyle': 11, 'Manager': 12, 'Maroc - G\xc3\xa9n\xc3\xa9riques': 13, 'Maroc - Renault': 38, 'Medicine': 14, 'M\xc3\xa9canicien': 39, 'M\xc3\xa9dical': 15, 'NL M\xc3\xa9dical': 37, 'NL Technique': 16, 'Nuit': 17, 'Prestataires': 51, 'RENAULT': 18, 'RTC': 49, 'Regulation Medicale': 19, 'R\xc3\xa9ception': 20, 'SAP': 21, 'Services': 22, 'TAI - CARTES': 23, 'TAI - PANNE MECANIQUE': 50, 'TAI - PNEUMATIQUES': 24, 'TAI - RISQUE': 25, 'TAI - RISQUE SERVICES': 26, 'TAI - SERVICE': 27, 'TPA': 28, 'Tech. Axa': 29, 'Tech. Inter': 30, 'Tech. Total': 36, 'Technical': 31, 'Technique Belgique': 32, 'Technique International': 33, 'Truck Assistance': 34, 'T\xc3\xa9l\xc3\xa9phonie': 35}

        self.default_columns = self.days.values()+self.months.values()+['TIME', 'ASS_ID']+['CSPL_RECEIVED_CALLS']
CONFIG = _Config()

print CONFIG.default_columns