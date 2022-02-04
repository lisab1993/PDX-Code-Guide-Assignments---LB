from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Tracking
import json

# Create your views here.


# def index(request):
#     #get every single book
#     all_books = Book.objects.all()

#     #create new lists to append to
#     availables = []
#     unavailables = []

#     #iterate over every book object in the queryset
#     for book in all_books:
#         #get the most recent checkout/checkin record for the individual book 
#         record = book.trackings.last()
#         #if the book exists, sort it by its checkout status
#         if record != None:
#             if record.checkout == False:
#                 #append the book, not the checkout/checkin record
#                 availables.append(book)
#             else:
#                 unavailables.append(book)
#         #if the book has never been checked out, it will automatically be made available
#         else:
#             availables.append(book)

#     #the lists made at the start are passed into the context object to be used in html
#     context = {
#         'availables': availables,
#         'unavailables': unavailables,
#     }
#     return render(request, 'libapp/base.html', context)




def index(request):
    all_books = Book.objects.available()
    print(all_books)
    # history = Tracking.objects.all().values()
    # book = get_object_or_404(Book, id=1)
    # print(book.available)

    # for book in all_books:
    #     print(book.available)


    context = {
    }
    return render(request, 'libapp/base.html', context)
