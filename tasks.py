from invoke import run, task


@task
def build():
    run('s3cmd --acl-public put index.html s3://www.djangopony.com/index.html')
    run('s3cmd --acl-public sync media/ s3://static.djangopony.com/')


@task
def runserver():
    run('python -m SimpleHTTPServer')
