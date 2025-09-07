#click_script
import click
from Repository import Repository
class CLI:
    def __init__(self,path):
        self.re=Repository(path)
    def create_cli(self):
        @click.group()
        def cli():
            """Management user interface repository"""
            pass
        @cli.command()
        def init():
            try:
                self.re.init()
                click.echo("Initialized repository structure.")
            except Exception as e:
                click.echo("Error"+str(e))
        @cli.command()
        @click.argument("file1")
        def add(file1):
            try:
                self.re.add(file1)
                click.echo("file added successfully.")
            except Exception as e:
                click.echo("Error" + str(e))
        @cli.command()
        @click.argument("message")
        def commit(message):
            try:
                self.re.commit(message)
                click.echo("Commited successfully.")
            except Exception as e:
                click.echo("Error" +str(e))
        @cli.command()
        def log():
            try:
                self.re.log()
            except Exception as e:
                click.echo("Error" +str(e))
        @cli.command()
        def status():
            try:
                self.re.status()
            except Exception as e:
                click.echo("Error" + str(e))
        @cli.command()
        @click.argument("id1")
        def checkout(id1):
            try:
                 self.re.checkout(id1)
            except Exception as e:
                click.echo("Error" +str(e))
        return cli