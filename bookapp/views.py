from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignupForm
# views.py
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book, UserBookStatus
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
# views.py
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


from .models import UserBookStatus



# Create your views here.
def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def classics(request):
    return render(request,'classics.html')

def contactus(request):
    return render(request,'contactus.html')

def dystopian(request):
    return render(request,'dystopian.html')

def fantasy(request):
    return render(request,'fantasy.html')



def mystery(request):
    return render(request,'mystery.html')

def non_fiction(request):
    return render(request,'non_fiction.html')

def sci_fic(request):
    return render(request,'sci_fic.html')



def dashboard(request):
    tbr_books = UserBookStatus.objects.filter(user=request.user, status='TBR')
    reading_books = UserBookStatus.objects.filter(user=request.user, status='Reading')
    completed_books = UserBookStatus.objects.filter(user=request.user, status='Completed')

    context = {
        'tbr_books': tbr_books,
        'reading_books': reading_books,
        'completed_books': completed_books,
    }

    return render(request, 'dashboard.html', context)






def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save user just yet
            user.set_password(form.cleaned_data['password1'])  # Set the hashed password
            user.save()  # Now save the user
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('dashboard')  # Redirect to the dashboard after successful sign-up
        else:
            messages.error(request, "There were some errors in the form. Please correct them and try again.")
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Stay on the login page if authentication fails
    else:
        return render(request, 'login.html')  # Show login form when GET request
    
def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')




@login_required
def get_user_books(request):
    user = request.user
    user_books = UserBookStatus.objects.filter(user=user)
    user_books_data = {
        'TBR': [],
        'Reading': [],
        'Completed': [],
    }
    
    # Organize books by their statuses
    for user_book in user_books:
        user_books_data[user_book.status].append(user_book.book)

    return JsonResponse(user_books_data)


GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes'

@login_required
def search_books(request):
    query = request.GET.get('query', '')
    if query:
        response = requests.get(GOOGLE_BOOKS_API_URL, params={'q': query})
        results = response.json().get('items', [])
        books = []
        for item in results:
            book_info = item['volumeInfo']
            book = {
                'id': item['id'],
                'title': book_info.get('title', 'No Title'),
                'author': ', '.join(book_info.get('authors', ['Unknown Author'])),
                'description': book_info.get('description', 'No description available'),
                'rating': book_info.get('averageRating', 0.0),
                'cover_url': book_info.get('imageLinks', {}).get('thumbnail', 'https://example.com/default-cover.jpg')
            }
            books.append(book)
        return JsonResponse({'books': books})
    return JsonResponse({'books': []})



from django.http import JsonResponse
from .forms import BookStatusForm
from .models import Book

@csrf_exempt
@api_view(['POST'])
def update_book_status(request):
    form = BookStatusForm(request.POST)

    if form.is_valid():
        book_id = form.cleaned_data['book_id']
        status = form.cleaned_data['status']

        try:
            book = Book.objects.get(id=book_id)
            book.status = status
            book.save()
            return JsonResponse({'status': 'success'})
        except Book.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid form data'}, status=400)


@login_required
def get_user_books(request):
    books = {
        'TBR': [],
        'Reading': [],
        'Completed': [],
    }
    
    user_books = UserBookStatus.objects.filter(user=request.user)
    for user_book in user_books:
        books[user_book.status].append({
            'id': user_book.book.id,
            'title': user_book.book.title,
            'author': user_book.book.author,
            'description': user_book.book.description,
            'rating': user_book.book.rating,
            'cover_url': user_book.book.cover_url
        })

    return JsonResponse(books)


















