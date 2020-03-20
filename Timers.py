# GPP: Timer class

from datetime import datetime

import math
import csv

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

    def unpause_timer(self):
        """unpause a paused timer"""

        self.latest_start = datetime.now()
    
    def pause_timer(self):
        """pause timer and update time on"""

        self.latest_end = datetime.now()
        new_time_on = self._time_dif(self.latest_start, self.latest_end)
        self.update_time_on(new_time_on)
        self.write_timer()

    def reset_time(self):
        """Reset timer time_on to zero"""

        self.time_on = 0.0
    
    def write_timer(self):
        """Write timer to CSV upon stopping or starting as backup"""

        with open(f'{self.matter}_timer_{self.date}.csv', mode='w') as csv_file:
            fieldnames = ['Matter', 'Date', 'Time_On', 'Latest_End', 'Narrative']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(self._timer_dict())
            
    def _time_dif(self, start, end):
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

    def _timer_dict(self):
        """Create dict of info for export"""

        timer_dict = {'Matter' : self.matter,
                        'Date' : self.date,
                        'Time_On' : self.time_on,
                        'Latest_End' : self.latest_end,
                        'Narrative' : self.narrative}
        return timer_dict