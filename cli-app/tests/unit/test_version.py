from app import __app_name__, __version__, cli

def test_version(runner):
    response = runner.invoke(cli.app, ["--version"])

    assert response.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in response.stdout