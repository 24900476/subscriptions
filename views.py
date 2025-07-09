from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscription
from .forms import SubscriptionForm
from django.contrib.auth.decorators import login_required

@login_required
def subscription_detail(request):
    # Show logged-in user's subscription or None
    subscription = getattr(request.user, 'subscription', None)
    return render(request, 'subscriptions/detail.html', {'subscription': subscription})

@login_required
def subscription_create_or_update(request):
    try:
        subscription = request.user.subscription
    except Subscription.DoesNotExist:
        subscription = None

    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.user = request.user
            sub.save()
            return redirect('subscription_detail')
    else:
        form = SubscriptionForm(instance=subscription)

    return render(request, 'subscriptions/form.html', {'form': form})
