#!/usr/bin/env python3
import subprocess
import sys
from argparse import ArgumentParser
from os import path

def main():
	parser = ArgumentParser(description="splits a file into M4A tracks")
	parser.add_argument("ffmpeg", action="store", type=str, help="path to ffmpeg")
	parser.add_argument("source", action="store", type=str, help="file to split")
	parser.add_argument("tracks", action="store", type=str, help="track info file")
	parser.add_argument("target", action="store", type=str, help="target folder")
	options = parser.parse_args()

	times, names = [], []
	with open(options.tracks, "r") as tracks:
		for track in [t.strip() for t in tracks]:
			fields = track.split("|")
			if len(fields) == 2:
				times.append(fields[0])
				if len(times) > 2:
					times = times[1:]

				if len(times) == 2:
					subprocess.call([
						options.ffmpeg, "-i", options.source, "-ss", times[0],
						"-vn", "-codec:a", "copy", "-sn", "-to", times[1],
						path.join(options.target, "{0:02d} - {1}.m4a".format(len(names), names[-1]))
					])

				names.append(fields[1])

	subprocess.call([
		options.ffmpeg, "-i", options.source, "-ss", times[-1],
		"-vn", "-codec:a", "copy", "-sn",
		path.join(options.target, "{0:02d} - {1}.m4a".format(len(names), names[-1]))
	])

	subprocess.call([
		options.ffmpeg, "-ss", times[-1], "-i", options.source,
		"-filter:v",  "thumbnail", "-frames:v",  "1",
		path.join(options.target, "folder.jpg")
	])

if __name__ == "__main__":
	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(1)
