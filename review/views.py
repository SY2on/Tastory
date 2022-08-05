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
        return render(request, 'review_write.html', {'form':form} )


def detail(request, Review_id):
    object_detail = get_object_or_404(Review, id = Review_id)         #id or pk?
    return render(request, 'review_detail.html', {'object_detail': object_detail})


def edit(request, Review_id) :
    review = Review.objects.get(id=Review_id)
    if request.method == 'POST' :
        review.title = request.POST['title']
        review.content = request.POST['content']
        review.status = request.POST['status']
        review.save()
        return redirect('review')
    
    else :
        form = ReviewForm()
        return render(request, 'review_edit.html', {'form':form} )
