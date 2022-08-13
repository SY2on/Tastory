from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Book
from common.models import User, Profile
from .forms import ReviewForm


@login_required
def write(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        book_id = request.session.get('book_id', 0)
        book = Book.objects.get(book_id=book_id)
        user = request.user
        new_review = form.save(user=user, book=book)
        return redirect('review_detail', review_id=new_review.review_id)
    else:
        book_id = request.session['book_id']
        book = get_object_or_404(Book, book_id=book_id)
        form = ReviewForm()
        context = {
            'form': form,
            'book': book,
            'user': user
        }
        return render(request, 'review/review_form.html', context)


def detail(request, review_id):
    review = get_object_or_404(Review, review_id=review_id)
    book = Book.objects.get(book_id=review.book_id)
    user = User.objects.get(user_id=review.user_id)
    context = {'review': review, 'book': book, 'user': user}
    print(context)
    return render(request, 'review/review_detail.html', context)


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
    qs = Book.objects.all()
    # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    q = request.GET.get('title', '')
    # 제목에 q가 포함되어 있는 레코드만 필터링
    if q:
        qs = list(qs.filter(title__icontains=q).values())
    else:
        qs = []
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
        print(book.author)
    return render(request, 'review/book_info.html', context)


def library(request, user_id):
    user = User.objects.get(user_id=user_id)
    profile = Profile.objects.get(user_id=user_id)
    reviews = Review.objects.filter(user_id=user_id)
    review_book_list = []
    for review in reviews:
        book = Book.objects.get(book_id=review.book_id)
        review_book_match = [review, book]
        review_book_list.append(review_book_match)
    context = {
        'review_book_list': review_book_list,
        'user': user,
        'profile': profile
    }
    print(user)
    print(profile)
    print(review_book_list)
    return render(request, "review/library.html", context)
