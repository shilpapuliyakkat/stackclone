from stack.models import Questions,Answers
def activities(request):
    if request.user.is_authenticated:
        cnt=Questions.objects.filter(user=request.user).count()
        ant=Answers.objects.filter(user=request.user).count()
        return{"qcnt":cnt,"aant":ant}
    else:
        return{"qcnt":0}