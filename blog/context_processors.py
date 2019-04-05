from .models import Category


def category_list(context):
    cat_list = Category.objects.all()
    return {'category_list': cat_list}