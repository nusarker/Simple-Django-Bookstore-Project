from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Book, Category, Review
from .forms import BookForm, CustomUserForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def book_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    books =  Book.objects.all()
    if query:
        books = books.filter(Q(title__icontains = query) | Q(author__icontains = query))


    if category_id:
        books = books.filter(category_id=category_id)
    paginator = Paginator(books, 6)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    categories = Category.objects.all()
    context = {
        'page_obj': page_obj,
        'query': query,
        'categories':categories,
        'selected_category':category_id,
    }
    return render(request, 'books/book_list.html', context)


@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form':form})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":

        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect("book_list")
        
    else:
        form = BookForm(instance = book)
    return render(request,'books/book_form.html', {'form':form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect("book_list")
        
    else:
        form = BookForm(instance = book)
    return render(request, 'books/confirm_delete.html', {'book': book})


def book_details(request, pk):
    book = get_object_or_404(Book, pk = pk)
    reviews = book.reviews.all()
    review_form  = None
    if request.user.is_authenticated:
        existing_review= Review.objects.filter(book=book, user=request.user).first()
        if request.method=='POST': 
            if existing_review:
                review_form = ReviewForm(request.POST, instance=existing_review)
            else:
                review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.user = request.user
                new_review.book = book
                new_review.save()
                return redirect('book_details', pk = pk)
            else:
                review_form = ReviewForm(instance=existing_review)
    return render(request, 'books/book_details.html', {'book': book,'reviews': reviews, 'review_form': review_form} )


def registration_view(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        
    else:
        form = CustomUserForm()
    return render(request, 'registration/registration.html', {'form':form})


@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk = pk)
    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_details', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'books/add_review.html', {'form': form, 'book':book})








    




