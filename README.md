# [xtraudio][1]

xtraudio is a [Python][2] script that splits any [FFmpeg][3] supported video
containing an AAC audio track into individual audio tracks and extracts a
thumbnail image from the video.

## Usage

```shell
$ ./xtraudio.py /usr/bin/ffmpeg video.mp4 tracks.txt extracted/
```

## Tracklisting Format

Tracklisting file must contain a single track per line and the lines must be
formatted by separating track start times from the track title by using a
vertical bar.

```
00:00|Track 1
03:15|Track 2
06:30|Track 3
```

## Output Filenames

Output filenames are genereted by using the track's sequence number as a zero
padded prefix followed by the track title separated by a hyphen. Tracklisting
used in the previous example would generate the following files.

```
01 - Track 1.m4a
02 - Track 2.m4a
03 - Track 3.m4a
```

[1]: https://github.com/scoobadog/xtraudio "xtraudio"
[2]: https://www.python.org/ "Python.org"
[3]: https://www.ffmpeg.org/ "FFmpeg"
