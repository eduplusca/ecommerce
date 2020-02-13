from __future__ import absolute_import

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from oscar.core.application import OscarConfig
from oscar.core.loading import get_class


class RefundsDashboardConfig(OscarConfig):
    label = 'refunds_dashboard'
    name = 'ecommerce.extensions.dashboard.refunds'
    namespace = 'refunds'
    verbose_name = _('Refunds Dashboard')
    default_permissions = ['is_staff', ]
    permissions_map = {
        'list': (['is_staff'], ['partner.dashboard_access']),
        'detail': (['is_staff'], ['partner.dashboard_access']),
    }

    # pylint: disable=attribute-defined-outside-init
    def ready(self):
        super().ready()
        self.refund_list_view = get_class('dashboard.refunds.views', 'RefundListView')
        self.refund_detail_view = get_class('dashboard.refunds.views', 'RefundDetailView')

    def get_urls(self):
        urls = [
            url(r'^$', self.refund_list_view.as_view(), name='list'),
            url(r'^(?P<pk>[\d]+)/$', self.refund_detail_view.as_view(), name='detail'),
        ]
        return self.post_process_urls(urls)
