from django.shortcuts import render
from . import forms
# Create your views here.
def thankyou(request):
    return render(request,'feedbackapp/thankyou.html')
def StudentFeedback(request):
    if request.method=='GET':
        form=forms.StudentRegForm()
        return render(request, 'feedbackapp/feedback.html', {'form':form})
    if request.method=='POST':
        form=forms.StudentRegForm(request.POST)
        if form.is_valid():
            print('form validation success and printing information')
            print('Name', form.cleaned_data['name'])
            print('Roll No.', form.cleaned_data['rollno'])
            print('Email', form.cleaned_data['email'])
            print('Feedback', form.cleaned_data['feedback'])
            ########or Second Method
            # print(request.POST['name'])
            # print(request.POST['rollno'])
            # print(request.POST['email'])
            # print(request.POST['feedback'])
            return thankyou(request)
        
    # return render(request,'feedbackapp/feedback.html',{'form':form})
