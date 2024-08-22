from django.shortcuts import render
from .tasks import add, mul

def add_two_nums(request):
    if request.method == 'POST':
        print(request.POST)
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        xxx = add.delay(num1,num2)
        mul.delay()
        context = {'msg': xxx}
        return render(request, 'index.html', context)
        
    return render(request, 'index.html')