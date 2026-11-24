import service
from config import LOCATIONS
from checklib import check, new_db, read_source
db = new_db()
check("0A-r3 地點清單有宿舍", "宿舍" in LOCATIONS, True)
check("0A-r3 可以在宿舍登記", service.report_found(db, "⾬傘", "宿舍")["ok"],
True)
check("0A-r3 LOCATIONS 只寫⼀次", read_source("config.py").count("LOCATIONS="), 1)