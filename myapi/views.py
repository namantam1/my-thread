from django.shortcuts import render,redirect,HttpResponse
from .models import Comment,Thread

def feedback(request, thread):
    print(request.user)
    if request.method=='POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email', "dummy@test.com")
        comment = data.get('comment')
        parent = data.get('id')
        parent = Comment.objects.filter(id=parent).first()
        user = request.user if request.user.is_authenticated else None
        threads = Thread.objects.filter(thread=thread).first()
        c = Comment(
            thread=threads,
            user=user,
            text=comment,
            name=name,
            email=email,
            parent=parent
        )
        c.save()
        print(c)
        return redirect('feedback',thread)
    threads = Thread.objects.filter(thread=thread).first()
    if not threads:
        return HttpResponse("Invalid thread Id", status=404)
    comments = threads.comment_set
    context = {
        'thread': thread,
        'feedback': 'active',
        'comments': comments.order_by("-created_on"),
        'commentcount': comments.filter(parent__isnull=True).count(),
        'answercount': comments.filter(parent__isnull=False).count()
    }
    return render(request, 'feedback.html', context=context)
