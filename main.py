import boto3
import json
import argparse
import os
import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips


# Args
parser = argparse.ArgumentParser()
parser.add_argument('creds_file')
parser.add_argument('video_names')
parser.add_argument('bucket_name')

# Get args
args = parser.parse_args()
file = args.creds_file
video_names = args.video_names.split()
bname = args.bucket_name


# Check if there is a creds json file, else break

# print(file, video_names)
if not os.path.isfile(file):
    raise ValueError(
        'Invalid json Filename, please create a creds.json file\nwith your ' +
        'server location, aws id, and aws secret'
        )

# Get the credentials

creds = None
with open('./creds.json', 'r') as f:
    creds = json.load(f)
reg = creds['server_location']
pkey = creds['id']
priv = creds['secret']

# Get the s3 instance
s3 = boto3.resource(
    service_name='s3',
    region_name=reg,
    aws_access_key_id=pkey,
    aws_secret_access_key=priv
)

# Get my specific bucket
video_bucket = s3.Bucket(bname)


# For each video in the names
# Download the video

for i, name in enumerate(video_names):
    ob = video_bucket.Object(name)
    ob.download_file('vid{}.mp4'.format(i))

# Open each video clip
video_files = [VideoFileClip('vid{}.mp4'.format(n))
               for n in range(len(video_names))]

# print(video_files)

# Merge the clips
merged_clip = concatenate_videoclips(video_files, method='compose')
merged_clip.write_videofile('merged_video.mp4')

# upload back to s3 bucket
video_bucket.upload_file(Filename='merged_video.mp4', Key='merge.mp4')
print('Merge Completed Successfully')


# Remove all tmp files
directory = os.getcwd()
for mp4 in glob.iglob(os.path.join(directory, '*.mp4')):
    print('Removing tmp file: {}\n'.format(mp4))
    os.remove(mp4)
