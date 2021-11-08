# youtube-cli

Setup:
```bash
export YOUTUBE_KEY=my_key
python -m venv .env
source .env/bin/activate
pip install -e .
```

Example usage:
```bash
yt-cli --help
yt-cli comments --video-id W86cTIoMv2U --save
yt-cli video --url https://www.youtube.com/watch?v=B-eeNvUEGDk
```

```
> yt-cli comments --help

Usage: yt-cli comments [OPTIONS]

Options:
  --video-id TEXT  the video id
  --url TEXT       video url
  --limit INTEGER  approximate max comments
  --replies        include comment replies
  --save           save to file (default is stdout)
  --help           Show this message and exit.
```

```
> yt-cli video --help

Usage: yt-cli video [OPTIONS]

Options:
  --video-id TEXT  the video id
  --url TEXT       video url
  --save           save to file (default is stdout)
  --help           Show this message and exit.
```

Get information about a channel:
```
> yt-cli channel info --username [USERNAME]
> yt-cli channel info --channel-id [CHANNEL_ID]
```

Get uploads from a channel:
```
> yt-cli channel uploads --username [USERNAME] --limit 100
> yt-cli channel uploads --channel-id [CHANNEL_ID]
```

Interactive:
```python
from src.comments import *
from src.helpers import *

smallest_cat = "W86cTIoMv2U"
top = get_comment_threads(smallest_cat)
save(top, smallest_cat, prefix="cat")
```

TODO
* get comment count from video api, show progress bar
* list videos i've listened to the most
* get bigger batches
