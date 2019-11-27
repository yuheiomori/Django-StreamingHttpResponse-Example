from django.shortcuts import render
from django.http.response import HttpResponse,StreamingHttpResponse
from books.models import Book
import csv
import io


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value



def index(request):
    return HttpResponse("<a href='/download/'>Download</a> <a href='/streaming_download/'>Streaming Download</a>")


def download(request):
    qs = Book.objects.all()
    csvfile = io.StringIO()
    writer = csv.writer(csvfile)
    for e in qs:
        writer.writerow((e.title, e.description))
    csvfile.seek(0)
    content = csvfile.getvalue()
    response = HttpResponse(content, content_type="text/csv", charset="sjis")
    response["Content-Disposition"] = 'attachment; filename="books.csv"'
    return response


def streaming_download(request):
    qs = Book.objects.all()
    echo = Echo()
    writer = csv.writer(echo)
    generator = (writer.writerow((e.title, e.description)) for e in qs)
    response = StreamingHttpResponse(generator, content_type="text/csv", charset="sjis")
    response["Content-Disposition"] = 'attachment; filename="books.csv"'
    return response