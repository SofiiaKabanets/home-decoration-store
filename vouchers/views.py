from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Voucher
from .forms import VoucherApplyForm

@require_POST
def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        voucher = get_object_or_404(
            Voucher,
            code__iexact=code,
            valid_from__lte=now,
            valid_to__gte=now,
            active=True
        )
        request.session['voucher_id'] = voucher.id
    else:
        request.session['voucher_id'] = None

    return redirect('cart:cart_detail')