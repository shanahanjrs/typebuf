from invoke import task


@task
def test(c):
    c.run('pytest -vvv --cov=typebuf --cov-report=html', pty=True)
