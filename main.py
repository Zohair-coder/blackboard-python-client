from bbrest import BbRest

import os
import json

key = os.environ["BLACKBOARD_APP_KEY"]
secret = os.environ["BLACKBOARD_SECRET"]
url = os.environ["BLACKBOARD_URL"]

bb = BbRest(key, secret, url, verify=False)

# print(bb.expiration())

courses = bb.GetCourses().json()["results"]
print(json.dumps(courses, indent=2))

# List all available functions
# print(json.dumps(list(bb.functions.keys()), indent=2))

