from datetime import datetime
from pathlib import Path

def get_week(d=datetime.today()):
    return (int(d.strftime("%W")) + 52 - 5) % 52

# default is 'primary', if you are using a separate calendar for your course schedule,
# your calendarId (which you can find by going to your Google Calendar settings, selecting
# the relevant calendar and scrolling down to Calendar ID) probably looks like
# xxxxxxxxxxxxxxxxxxxxxxxxxg@group.calendar.google.com
# example:
# USERCALENDARID = 'xxxxxxxxxxxxxxxxxxxxxxxxxg@group.calendar.google.com'
USERCALENDARID = 'primary'
CURRENT_COURSE_SYMLINK = Path('/home/forrekenn/current_course').expanduser()
CURRENT_COURSE_ROOT = CURRENT_COURSE_SYMLINK.resolve()
CURRENT_COURSE_WATCH_FILE = Path('/tmp/current_course').resolve()
ROOT = Path('~/Documents/math-notes/bachelors/spring-2025').expanduser()
DATE_FORMAT = '%A %d %B %Y'


