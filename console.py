import click

from comments import get_comment_threads, save as _save


@click.group()
@click.option("--api-key", envvar="YOUTUBE_KEY")
@click.pass_context
def cli(ctx, api_key):
    ctx.obj = {"api_key": api_key}


@click.command()
@click.option("--video-id", help="the video id")
@click.pass_context
def test(ctx, video_id):
    click.echo(f"Getting comments for {video_id=}, {ctx.obj['api_key']=}")


@click.command()
@click.option("--video-id", help="the video id")
@click.option("--save", is_flag=True)
def comments(video_id, save):
    top = get_comment_threads(video_id)
    if save:
        _save(top, video_id)
    else:
        click.echo(top)


cli.add_command(comments)
cli.add_command(test)
