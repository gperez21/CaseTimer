from datetime import datetime

import math

class Timer:
    def __init__(self, matter, narrative):
        self.matter = matter
        self.time_on = 0.0
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.narrative = narrative
        self.latest_start = datetime.now()
        self.latest_end = datetime.now()

    def update_time_on(self, new_time):
        """Update timer time hours to tenth hr. precision"""
        prev_time_on = self.time_on
        self.time_on = new_time + prev_time_on

    def update_matter(self, new_matter):
        """Update timer matter"""

        self.matter = new_matter
    
    def update_narrative(self, new_narrative):
        """Update timer matter"""

        self.matter = new_narrative

    def stop_timer(self):
        """Stop timer and update time on"""
        self.latest_end = datetime.now()
        new_time_on = _time_dif(self.latest_start, self.latest_end)
        update_time_on(new_time_on)

    def reset_time(self):
        """Reset timer time_on to zero"""
        self.time_on = 0.0

    def _time_dif(start, end):
        """Time timer has been runnning

        subtract newwest start from newest end and then convert to x.x hours
        """
        
        diff = end - start
        seconds = diff.seconds
        minutes = math.ceil(seconds/60.0)
        hour_whole = math.floor(minutes/60.0)
        # round up to nearest 1/10th hour
        hour_fract = math.ceil((minutes%60)/6)/10.0
        new_time_on = hour_whole + hour_fract
        return new_time_on