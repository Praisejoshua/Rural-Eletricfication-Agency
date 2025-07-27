from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'complaint_name', 'department', 'problem',
            'problem_description', 'ict_response',
            'complain_satisfy', 'unsatisfied_reason',
            'signed_by_staff', 'signed_by_hod_ict', 'signed_by_head_section'
        ]

    def clean(self):
        cleaned_data = super().clean()
        satisfy = cleaned_data.get('complain_satisfy')
        reason = cleaned_data.get('unsatisfied_reason')

        if satisfy == 'no' and not reason:
            self.add_error('unsatisfied_reason', 'Please provide a reason for dissatisfaction.')

        return cleaned_data
