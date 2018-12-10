from django.utils.safestring import mark_safe
from wagtail.admin.site_summary import PagesSummaryItem
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from wagtail.core import hooks
from home.models import Author, Book


# https://docs.wagtail.io/en/latest/reference/hooks.html#construct-main-menu
@hooks.register('construct_main_menu')
def hide_explorer_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'explorer']


# https://docs.wagtail.io/en/latest/reference/hooks.html#construct-homepage-summary-items
@hooks.register('construct_homepage_summary_items')
def remove_pages_summary_item(request, summary_items):
    summary_items[:] = [i for i in summary_items if not isinstance(i, PagesSummaryItem)]


@hooks.register('insert_global_admin_css')
def customize_admin_colours():
    return mark_safe("""<style>
:root {
  --main-bg-color: #343F4C;
  --primary-color: #1C86BA;
  --accent-color: #36A3D9;
}
header {
  background-color: var(--main-bg-color);
}
a {
  color: var(--primary-color);
}
a:hover {
  color: var(--accent-color);
}
.button,
header .button {
  background-color: var(--primary-color);
  border-color: var(--main-bg-color);
}
.button:hover,
.replace-file-input:hover button {
  background-color: var(--primary-color) !important;
}
.button-secondary {
  color: var(--main-bg-color);
}
</style>""")


class AuthorAdmin(ModelAdmin):
    model = Author
    menu_label = 'Author'
    menu_icon = 'user'


class BookAdmin(ModelAdmin):
    model = Book
    menu_label = 'Book'
    menu_icon = 'form'


modeladmin_register(AuthorAdmin)
modeladmin_register(BookAdmin)
