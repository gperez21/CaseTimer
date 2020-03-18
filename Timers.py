from datetime import datetime

class Timer:
    def __init__(self, matter, narrative):
        self.matter = matter
        self.time_on = 0.0
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.narrative = narrative
        self.latest_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.latest_end = "NULL"

    def update_time(self, new_time):
        """Update timer time"""
        self.time_on = new_time

    def update_matter(self, new_matter):
        """Update timer matter"""

        self.matter = new_matter
    
    def update_narrative(self, new_narrative):
        """Update timer matter"""

        self.matter = new_narrative
