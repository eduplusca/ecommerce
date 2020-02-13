from __future__ import absolute_import

from oscar import config

from .utils import exclude_app_urls


class EdxShop(config.Shop):
    name = "ecommerce"
    # URLs are only visible to users with staff permissions
    default_permissions = 'is_staff'

    # TODO -- I will remove it later.
    # def ready(self):
    #    super().ready()
    #    Override core app instances with blank application instances to exclude their URLs.
    #    promotions_app = Application()
    #    catalogue_app = Application()
    #    search_app = Application()

    def get_urls(self):
        urls = super().get_urls()
        # excluding urls of catalogue and search
        exclude_app_urls(urls, 'catalogue')
        exclude_app_urls(urls, 'search')

        return urls
