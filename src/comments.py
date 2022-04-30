from dataclasses import dataclass, field
import json
from typing import List

from .helpers import YOUTUBE_CLIENT as YT


@dataclass
class Comment:
    id: str
    text: str


@dataclass
class TopLevelComment(Comment):
    replies: List[Comment] = field(default_factory=list)


@dataclass
class CommentThread:
    comments: List[TopLevelComment]

    def extend(self, thread):
        self.comments.extend(thread.comments)

    @property
    def size(self):
        return sum(1 + len(c.replies) for c in self.comments)


def get_threads(video_id, page_token=None):

    request = YT.commentThreads().list(
        part="snippet,replies", videoId=video_id, pageToken=page_token, maxResults=100
    )
    try:
        return request.execute()
    except Exception as e:
        print(f"Failed request for thread: {e}")
        return {}


def _get_child_comments(parent_id):
    request = YT.comments().list(part="snippet", parentId=parent_id, maxResults=100)
    try:
        return request.execute()
    except Exception as e:
        print(f"Failed request for replies: {e}")
        return {}


def extract_text(filename, rename=None):
    with open(filename) as f:
        orig = json.load(f)
        filtered = [c["text"] for c in orig["comments"]]
    if rename is not None:
        filename = rename
    with open(filename, "w") as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)


def extract_top(resp):
    comments = [x["snippet"]["topLevelComment"] for x in resp.get("items", [])]
    top = [TopLevelComment(c["id"], c["snippet"]["textOriginal"]) for c in comments]
    return CommentThread(top)


def get_comment_threads(video_id, replies=True, limit=None):
    some_threads = get_threads(video_id)
    token = some_threads.get("nextPageToken")
    result = extract_top(some_threads)
    page_count = 1
    while token is not None:
        if limit is not None and result.size >= limit:
            break
        more_threads = get_threads(video_id, token)
        token = more_threads.get("nextPageToken")
        thread = extract_top(more_threads)
        if replies:
            get_children(thread)
        result.extend(thread)
        print(f"got page {page_count}", end="\r")
        page_count += 1
    return result


def extract_children(resp):
    return [
        TopLevelComment(c["id"], c["snippet"]["textOriginal"])
        for c in resp.get("items", [])
    ]


def get_children(thread):
    for c in thread.comments:
        replies = _get_child_comments(c.id)
        c.replies.append(extract_children(replies))
