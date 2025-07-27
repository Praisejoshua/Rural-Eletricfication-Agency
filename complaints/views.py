from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from .models import Ticket

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket-list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'tickets/ticket_detail.html'



# This view generates a PDF of the ticket details



def ticket_pdf_view(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    template = get_template('tickets/ticket_pdf.html')
    html = template.render({'ticket': ticket})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{ticket.ticket_number}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors with PDF generation <pre>' + html + '</pre>')
    return response

