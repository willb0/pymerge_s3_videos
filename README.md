# pymerge_s3_videos
## This is a quick CLI tool I threw together to merge some videos in an s3 bucket using python, moviePy, and boto3

### Python requirements

```python
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
### AWS requirements
This tool assumes that you have both created a user to access your AWS resources 
and also have both your access key and the private access key
If you need help, check this [link](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) out 
Once you have your credentials, store them in a creds.json file

```json
{
"id":"your access key",
"secret":"your secret key",
"server_location":"us-east-2",
}
```

### AWS storage
Upload as many videos as youd like to an s3 bucket, take note of their filenames
I used two small videos in my example 

### Run script
To run the script, make sure you are in the directory with env activated and run:
```zsh
python main.py [creds_file] [video_names] [bucket_name]
```
where creds_file is your creds.json path,
video names is a string (important to pass a string),
and bucket_name is the name of your bucket
for example, 
```zsh
python main.py creds.json "videotest1.mp4 videotest2.mp4" aws-bucket-videos
```


