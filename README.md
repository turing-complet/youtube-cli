# youtube-cli

```python
import os

os.environ["YOUTUBE_KEY"] = "API_KEY"

from comments import *

smallest_cat = "W86cTIoMv2U"
top = get_comment_threads(smallest_cat)
save(top, "cat", smallest_cat)
```

TODO
* sort channel vids by popularity
* get comment count from video api, show progress bar
