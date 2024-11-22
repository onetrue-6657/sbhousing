from flask_frozen import Freezer
from flaskr import create_app

app = create_app()
freezer = Freezer(app)

@freezer.register_generator
def skip_dynamic_routes():
    yield '/auth/logout'

@freezer.register_generator
def static_routes():
    yield '/auth/register'
    yield '/auth/login'
    yield '/auth/logout'
    yield '/create'
    for post_id in range(1, 1001):
        yield f'/{post_id}/update'

@freezer.register_generator
def update_routes():
    for post_id in range(1, 1001):
        yield 'blog.update', {'id': post_id}

if __name__ == '__main__':
    freezer.freeze()