from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FormModel
from .forms import ResumeForm, ContactForm
import pdfkit
from django.template.loader import render_to_string

# Create your views here.
def create__profile__view(request):
    form = ResumeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('all-resumes')
    
    context = {'form': form}
    return render(request, 'create-resume.html', context)

def profile__detail__view(request, id):
    resume = get_object_or_404(FormModel, id=id)
    return render(request, 'resume.html', {'resume': resume})

def all__resumes__view(request):
    resumes = FormModel.objects.all()
    return render(request, 'all-resumes.html', {"resumes": resumes})

def download__pdf__view(request, id):
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    resume = get_object_or_404(FormModel, id=id)
    html = render_to_string('pdf-template.html', {'resume': resume})
    output= pdfkit.from_string(html, output_path=False, configuration=config)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    response.write(output)
    return response

def contact__view(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        contact = form.save()

        html_message = render_to_string('email.html', {
            'username': contact.username
        })

        email_message = EmailMessage(
                subject="Yeni Müraciət",
                body=html_message,
                from_email="ilhamzeynalov65@gmail.com",
                to=[contact.email],
            )

        email_message.content_subtype = "html"
        email_message.send()

        return redirect("contact")

    
    context = {'form': form}
    return render(request, 'contact.html', context)