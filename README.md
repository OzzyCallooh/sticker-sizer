# sticker-sizer

Python tool to resize a directory of images in bulk, invoking [ffmpeg](https://ffmpeg.org/) to do the actual image resizing.

Resized files are saved with the size postpended to the name, under the same extension. For example, **sticker.png** is saved to **sticker-512x512.png**. Files which already end with the size are skipped, so re-running the program will not attempt to resize images to the same size.

Requires: [click](https://click.palletsprojects.com/)

## Usage

```bash
python sticker-sizer.py PATH [--size 512x512] [--ext .png]
```

Provide a path to a directory of sticker files. Options:

- `--size`: format `WxH`, default `512x512`
- `--ext`: output file extension, if you want a specific one (e.g. convert to png)
- `--help`: More info

## Example (bash)

```bash
$ ls stickers
sticker.png

$ python sticker-sizer.py stickers --size 512x512
Input path: stickers
Size: 512x512
1 of 1: sticker.png => Converted (sticker-512x512.png)
Processed: 1 of 1

$ python sticker-sizer.py stickers --size 512x512
Input path: stickers
Size: 512x512
1 of 2: sticker-512x512.png => Skipped
2 of 2: sticker.png => Converted (sticker-512x512.png)
Processed: 1 of 2
```
