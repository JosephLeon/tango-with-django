import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat(name="Python")
    # python_cat = add_cat(
    #     name='Python',
    #     cat_views=128,
    #     cat_likes=64)

    add_page(
        cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(
        cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(
        cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat(name="Django")
    # django_cat = add_cat(
    #     name="Django",
    #     cat_views=64,
    #     cat_likes=32)

    add_page(
        cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(
        cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(
        cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat(name="Other Frameworks")
    # frame_cat = add_cat(
    #     name="Other Frameworks",
    #     cat_views=32,
    #     cat_likes=16)

    add_page(
        cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(
        cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


# def add_cat(name, cat_views, cat_likes):
#     c = Category.objects.get_or_create(name=name, cat_views=cat_views, cat_likes=cat_likes)[0]
#     return c


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
    print "Finished."
