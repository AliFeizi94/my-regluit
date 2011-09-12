from random import randint, randrange
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from regluit.core.models import Work, Campaign

class Command(BaseCommand):
    help = "creates random campaigns for any works that lack one for testing"

    def handle(self, *args, **options):
        for work in Work.objects.all():
            if work.campaigns.all().count() > 0:
                continue
            campaign = Campaign()
            campaign.name = work.title
            campaign.work = work
            campaign.description = "Test Campaign"

            # random campaign target between $200 and $10,000
            campaign.target = float(randint(200,10000))

            # random deadline between 5 days from now and 180 days from now
            now = datetime.now()
            campaign.deadline = random_date(now + timedelta(days=5),
                                            now + timedelta(days=180))

            campaign.save()
            print "created %s" % campaign


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return (start + timedelta(seconds=random_second))

