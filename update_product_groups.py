import os
import django

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "runnerreads.settings")
django.setup()

from reads.models import Book
from reads.amazon import Amazon

def run():
    amazon = Amazon()
    for book in Book.objects.all():
        print(book.title)
        product = amazon.lookup(book.ASIN)
        book.product_group = product.product_group
        print(book.product_group)
        book.save()
        print('------ saved ------')

if __name__ == '__main__':
    run()