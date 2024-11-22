from flask_frozen import Freezer
from flaskr import create_app

app = create_app()
freezer = Freezer(app)

@freezer.register_generator
def generate_routes():
    # 静态页面的路由
    yield '/'
    yield '/auth/register/'
    yield '/auth/login/'
    yield '/create/'

@freezer.register_generator
def dynamic_routes():
    for post_id in range(1, 1001):
        yield 'blog.update', {'id': post_id}

@freezer.register_generator
def skip_dynamic_routes():
    yield '/auth/logout/'

if __name__ == '__main__':
    for url in freezer.freeze_yield():
        print(f"Freezing URL: {url}")  # 打印每个生成的 URL
    freezer.freeze()
