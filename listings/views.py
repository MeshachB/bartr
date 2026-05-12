from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Listing
from .forms import ListingForm


def home(request):
    listings = Listing.objects.all()

    return render(
        request,
        'base.html',
        {'listings': listings}
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request,
        'signup.html',
        {'form': form}
    )


@login_required
def create_listing(request):

    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()

            return redirect('home')

    else:
        form = ListingForm()

    return render(
        request,
        'create_listing.html',
        {'form': form}
    )


@login_required
def update_listing(request, listing_id):

    listing = Listing.objects.get(id=listing_id)

    if listing.owner != request.user:
        return redirect('home')

    if request.method == 'POST':

        form = ListingForm(
            request.POST,
            instance=listing
        )

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = ListingForm(instance=listing)

    return render(
        request,
        'update_listing.html',
        {'form': form}
    )


@login_required
def delete_listing(request, listing_id):

    listing = Listing.objects.get(id=listing_id)

    if listing.owner == request.user:
        listing.delete()

    return redirect('home') 

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listing_detail.html', {'listing': listing})