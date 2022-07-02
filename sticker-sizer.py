import click
from pathlib import Path
import subprocess

# additional arguments sent to ffmpeg
ffmpeg_args = [
	'-y' # overwrite existing
]

SKIPPED = 'Skipped'
CONVERTED = 'Converted'
FAILED = 'Failed'

supported_extensions = ['.png', '.jpg', '.jpeg', '.gif']


def process_file(img_path, size, ext=None):
	ending = '-' + size
	suffix = ext if ext is not None else img_path.suffix
	out_img_path = img_path.parent / (img_path.stem + ending + suffix)

	if img_path.stem.endswith(ending):
		return SKIPPED, out_img_path

	if img_path.suffix not in supported_extensions:
		return SKIPPED, out_img_path

	args = ['ffmpeg', '-i', str(img_path), '-s', size, out_img_path] + ffmpeg_args
	completed_process = subprocess.run(args, capture_output=True)

	return CONVERTED if completed_process.returncode == 0 else FAILED, out_img_path


@click.command()
@click.argument('path', type=click.Path(exists=True, path_type=Path))
@click.option('--size', '-s', default='512x512', help='Desired size in the format WxH')
@click.option('--ext', '-e', type=click.Choice(supported_extensions), help='Desired extension', default=None)
def main(path, size, ext):
	"""Resize a directory of images"""
	click.echo('Input path: ' + str(path))
	click.echo('Size: ' + size)
	if ext:
		click.echo('Extension: ' + ext)

	successes = 0
	files_to_convert = list(path.glob('*.*'))
	for i, img_path in enumerate(files_to_convert):
		result, out_img_path = process_file(img_path, size=size, ext=ext)
		if result == CONVERTED:
			successes += 1
		# Resize status
		click.echo(
			'{} of {}: {} => {}'.format(
				i+1,
				len(files_to_convert),
				img_path.name,
				'{} ({})'.format(
					result,
					out_img_path.name
				) if result == CONVERTED else result, out_img_path.name
			)
		)
	# Total results
	click.echo(
		'Processed: {} of {}'.format(
			successes,
			len(files_to_convert)
		)
	)


if __name__ == '__main__':
	main()
