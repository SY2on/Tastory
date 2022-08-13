from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Book
from .forms import ReviewForm


@login_required
def write(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        new_review = form.save(commit=False)
        new_review.book_id = request.session.get('book_id', 0)
        new_review.user_id = request.user.user_id
        return redirect('review_detail', review_id=new_review.review_id)
    else:
        book_id = request.session['book_id']
        book = get_object_or_404(Book, book_id=book_id)
        form = ReviewForm()
        context = {
            'form': form,
            'book': book
        }
        return render(request, 'review/review_form.html', context)


def detail(request, review_id):
    review_detail = get_object_or_404(Review, review_id=review_id)
    return render(request, 'review/review_detail.html', {'review_detail': review_detail})


def edit(request, review_id):
    review = Review.objects.get(review_id=review_id)
    if request.method == 'POST':
        review.title = request.POST['title']
        review.content = request.POST['content']
        review.save()
        return redirect('review/review-detail', review_id=review_id)

    else:
        book = Review.objects.get(book_id=review.book_id)
        form = ReviewForm(instance=review)
        context = {
            'form': form,
            'book': book
        }
        return render(request, 'review/review_update_form.html', context)


def main(request):
    books = list(Book.objects.all().values())
    reviews = list(Review.objects.all().values())

    context = {
        "books": books,
        "reviews": reviews
    }
    return render(request, 'review/index.html',  context)


def search(request):
    qs = list(Book.objects.all().values())

    # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    q = request.GET.get('title', '')
    if q:
        qs = list(qs.filter(title__icontains=q).values())  # 제목에 q가 포함되어 있는 레코드만 필터링

    context = {
        'books': qs,
        'q': q
    }
    return render(request, 'review/search.html', context)


def bookinfo(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts_login')
        else:
            request.session['book_id'] = book_id
            return redirect('review_write')
    else:
        reviews = list(Review.objects.filter(book_id=book_id).values())

        context = {
            'book': book,
            'reviews': reviews
        }
    return render(request, 'review/book_info.html', context)


def library(request, user_id):
    reviews = Review.objects.filter(user_id=user_id)
    books = []
    for review in reviews:
        book = Book.objects.get(book_id=review.book_id)
        books.append(book)
    return render(request, "review/library.html", books)
