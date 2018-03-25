from jinja2 import Environment, PackageLoader

def print_tex(messages, users_info):
    env = Environment(loader=PackageLoader('latex', 'templates'))
    template = env.get_template('book.tex')
    print template.render(messages=messages, users=users_info)
