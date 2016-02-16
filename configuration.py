class _Config:
    def __init__(self):
        # All samples
        self.useful_columns = ['DATE', 'DAY_OFF', 'DAY_DS', 'WEEK_END', 'DAY_WE_DS', 'ASS_ASSIGNMENT', 'CSPL_CALLS']
        self.months = { 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

CONFIG = _Config()