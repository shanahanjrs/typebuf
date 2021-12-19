from invoke import task


@task
def test(c):
    c.run('pytest --cov=typebuf --cov-report=html', pty=True)
