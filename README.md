# youtube-cli

Setup:
```bash
export YOUTUBE_KEY=my_key
python -m venv .env
source .env/bin/activate
pip install -e .
```

Cli usage:
```bash
yt-cli --help
yt-cli comments --video-id W86cTIoMv2U
```

Interactive:
```python
import os
from comments import *

smallest_cat = "W86cTIoMv2U"
top = get_comment_threads(smallest_cat)
save(top, smallest_cat, prefix="cat")
```

TODO
* sort channel vids by popularity
* get comment count from video api, show progress bar
