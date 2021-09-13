# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery


def get_comments(video_id):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(part="snippet,replies", videoId=video_id)
    response = request.execute()

    ids = [x["snippet"]["topLevelComment"]["id"] for x in response["items"]]
    children = []
    for id in ids:
        request = youtube.comments().list(part="snippet", parentId=id)
        children.append(request.execute())

    return response, children
