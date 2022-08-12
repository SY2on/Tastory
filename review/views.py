from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Book
from .forms import ReviewForm
from django.core.paginator import Paginator


def write(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        new_review = form.save()
        return redirect('review_detail', review_id=new_review.review_id)
    else:
        form = ReviewForm()
        return render(request, 'review/review_form.html', {'form': form})


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
        form = ReviewForm(instance=review)
        return render(request, 'review/review_update_form.html', {'form': form})


def main(request):
    books = Book.objects.all()
    reviews = Review.objects.all()

    context = {
        "books": books,
        "reviews": reviews
    }
    return render(request, 'review/review_update_form.html',  context)


def search(request):
    qs = Book.objects.all()

    # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    q = request.GET.get('title', '')
    if q:
        qs = qs.filter(title__icontains=q)  # 제목에 q가 포함되어 있는 레코드만 필터링

    context = {
        'books': qs,
        'q': q
    }
    return render(request, 'review/index.html', context)


def bookinfo(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts_login')
        else:
            return redirect('review_write', book_id=book.book_id)
    # 로그인할시 리뷰작성 페이지로 넘어가는 코드
    else:
        reviews = Review.objects.filter(book_id=book_id)

        context = {
            'book': book,
            'reviews': reviews
        }
    return render(request, 'review/book_info.html', context)
