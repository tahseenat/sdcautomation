
import pytrends
from pytrends.request import TrendReq

# google_username = "mrandmissvibgyor@gmail.com"
# google_password = ""
# pyGTrends(google_username, google_password)

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['nike shoes'])

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())