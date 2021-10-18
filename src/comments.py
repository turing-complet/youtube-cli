from .helpers import YOUTUBE_CLIENT as YT


def _get_comment_threads(video_id, page_token=None):

    request = YT.commentThreads().list(
        part="snippet,replies", videoId=video_id, pageToken=page_token
    )
    return request.execute()


def extract_top(resp):
    comments = [x["snippet"]["topLevelComment"] for x in resp["items"]]
    return [{"id": c["id"], "original": c["snippet"]["textOriginal"]} for c in comments]


def get_comment_threads(video_id):
    some_threads = _get_comment_threads(video_id)
    token = some_threads["nextPageToken"]
    result = extract_top(some_threads)
    page_count = 1
    while token is not None:
        more_threads = _get_comment_threads(video_id, token)
        token = more_threads.get("nextPageToken")
        result.extend(extract_top(more_threads))
        print(f"got page {page_count}", end="\r")
        page_count += 1
    return result


def get_children(resp):
    ids = [x["snippet"]["topLevelComment"]["id"] for x in resp["items"]]
    children = []
    for id in ids:
        child = get_child_comments(id)
        children.append(child)

    return children


def get_child_comments(parent_id):
    request = YT.comments().list(part="snippet", parentId=parent_id)
    response = request.execute()
    return response
