from django.shortcuts import render
from celery.result import AsyncResult
from core.celery import add
from myapp.tasks import sub

# Enqueue Task using delay()
# def index(request):
#     print("Request index")
#     # result1 = add(10, 20)
#     # print(result1)
#     result2 = add.delay(10, 20)
#     print(result2)
#     result3 = sub.delay(10, 20)
#     print(result3)
#     return render(request, "myapp/index.html")

# Enqueue Task using apply_async()
# def index(request):
#     print("Request index")
#     result2 = add.apply_async(args=[10, 20])
#     print(result2)
#     result3 = sub.apply_async(args=[40, 20])
#     print(result3)
#     return render(request, "myapp/index.html")


# display value after execution
def index(request):
    print("Request index")
    result2 = add.delay(10, 20)
    print(result2)
    result3 = sub.delay(10, 20)
    print(result3)
    

    
    return render(request, "myapp/index.html", {"result2": result2, "result3": result3})

def about(request):
    print("Request about")
    return render(request, "myapp/about.html")

def contact(request):
    print("Request contact")
    return render(request, "myapp/contact.html")

def check_result(request, task_id):
    print("Request result")
    result = AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    # print("Get: ", result.get())
    return render(request, "myapp/result.html", {"result2": result})