import click, os

def register(app):
    @app.cli.group()
    def blueprint():
        """Blueprint creation commands"""
        pass

    @blueprint.command()
    @click.argument('name')
    def create(name):
        """Create new FLask blueprint"""
        bp_dir = os.path.abspath(os.path.dirname(__name__)) + f'/app/blueprints/{name}'
        try:
            if not os.path.exists(bp_dir):
                os.makedirs(bp_dir)
            init_file = open(f'{bp_dir}/__init__.py', 'w')
            init_file.close()

            routes_file = open(f'{bp_dir}/routes.py', 'w')
            routes_file.close()

            models_file = open(f'{bp_dir}/models.py', 'w')
            models_file.close()
        except:
            pass