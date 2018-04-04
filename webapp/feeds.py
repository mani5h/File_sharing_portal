from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from webapp.models import Notification


class LatestNotificationFeed(Feed):
    title= 'Mython'
    link = "//"
    description = "Updates on notifications in Mython app "

    def items(self):
        return Notification.objects.order_by('-pk')[:5]

    def item_title(self, item):
        return Notification.body

    def item_description(self, item):
        return Notification.body

    def item_link(self, item):
        return reverse('webapp:notification',kwargs={'nid':item.pk})