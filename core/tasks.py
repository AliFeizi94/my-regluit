from time import sleep
import logging
logger = logging.getLogger(__name__)

from celery.task import task

from django.contrib.auth.models import User

from regluit.core import bookloader, models
from regluit.core import goodreads, librarything

@task 
def populate_edition(isbn):
    """given an edition this task will populate the database with additional
    information about related editions and subjects related to this edition
    """
    bookloader.add_related(isbn)
    edition=models.Edition.get_by_isbn(isbn)
    if edition:
        bookloader.add_openlibrary(edition.work)
    return edition

@task
def load_goodreads_shelf_into_wishlist(user_id, shelf_name='all', goodreads_user_id=None, max_books=None,
                                       expected_number_of_books=None):
    user=User.objects.get(id=user_id)
    return goodreads.load_goodreads_shelf_into_wishlist(user,shelf_name,goodreads_user_id,max_books, expected_number_of_books)

@task
def load_librarything_into_wishlist(user_id, lt_username, max_books=None):
    user=User.objects.get(id=user_id)
    return librarything.load_librarything_into_wishlist(user, lt_username, max_books)
    
@task
def fac(n, sleep_interval=None):
    # used to test celery task execution 
    if not(isinstance(n,int) and n >= 0):
        raise Exception("You can't calculate a factorial of %s " % (str(n)))
    if n <= 1:
        return 1
    else:
        res = 1
        for i in xrange(2,n+1):
            res = res*i
            fac.update_state(state="PROGRESS", meta={"current": i, "total": n})
            if sleep_interval is not None:
                sleep(sleep_interval)
        return res

from django.core import mail

@task
def send_mail_task(subject, message, from_email, recipient_list,
	        fail_silently=False, auth_user=None, auth_password=None,
	        connection=None):
    """a task to drop django.core.mail.send_mail into """
    return mail.send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection)
    

from notification.engine import send_all
 
@task
def emit_notifications():
    logger.info('notifications emitting' )
    send_all()
