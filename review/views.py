from django.shortcuts import render, get_object_or_404, redirect
from .models import Review 
from .forms import ReviewForm

def write(request) :
    if request.method == 'POST' :
        form = ReviewForm(request.POST)
        new_review = form.save()
        return redirect('page-read', review_id = new_review.id)
    else :
        form = ReviewForm()
        return render(request, 'review/review_form.html', {'form':form} )


def detail(request, review_id):
    review_detail = get_object_or_404(Review, id = review_id)         
    return render(request, 'review/review_detail.html', {'review_detail': review_detail})


def edit(request, review_id) :
    review = Review.objects.get(id=review_id)
    if request.method == 'POST' :
        review.title = request.POST['title']
        review.content = request.POST['content']
        review.save()
        return redirect('review/review-detail', review_id = review_id)
    
    else :
        form = ReviewForm(instance=review)
        return render(request, 'review/review_update_form.html', {'form':form} )
