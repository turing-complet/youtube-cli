import click


@click.group()
def cli():
    pass


@click.command()
@click.option("--video-id", help="the video id")
def comments(video_id):
    click.echo(f"Getting comments for {video_id=}")


cli.add_command(comments)
