from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.utils import timezone

from django.db.models import Q
from .forms import ContactForm, ProgramApplicationForm
from .models import Blog, Talent, Event, Gallery


def home(request):
    events = Event.objects.filter(is_featured=True).order_by('-event_date')[:10]
    context = {
        'events': events,
        'upcoming_events': [
            {'title': 'Acoustic Night in Musanze', 'date': 'Friday, 18 July', 'summary': 'A live evening featuring emerging and established performers.'},
            {'title': 'Youth Talent Showcase', 'date': 'Saturday, 26 July', 'summary': 'A stage for promising creatives to perform and connect.'},
            {'title': 'Creative Entrepreneurship Bootcamp', 'date': 'Monday, 4 August', 'summary': 'Hands-on sessions on turning creativity into opportunity.'},
        ]
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def programs(request):
    return render(request, 'core/programs.html')


def apply(request):
    if request.method == 'POST':
        form = ProgramApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your application! We will review it and get back to you soon.')
            return redirect('apply')
    else:
        form = ProgramApplicationForm()
    return render(request, 'core/apply.html', {'form': form})


def events(request):
    from .models import Category
    selected_category = request.GET.get('category', '').strip()
    now = timezone.now()
    upcoming_events = Event.objects.filter(event_date__gte=now).order_by('event_date')
    past_events = Event.objects.filter(event_date__lt=now).order_by('-event_date')

    if selected_category:
        upcoming_events = upcoming_events.filter(category__name__iexact=selected_category)
        past_events = past_events.filter(category__name__iexact=selected_category)

    featured_event = upcoming_events.first()
    categories = Category.objects.all()
    upcoming_events_limited = upcoming_events[:3]
    past_events_limited = past_events[:3]
    return render(request, 'core/events.html', {
        'featured_event': featured_event,
        'upcoming_events': upcoming_events_limited,
        'more_upcoming': upcoming_events.count() > 3,
        'past_events': past_events_limited,
        'more_past': past_events.count() > 3,
        'categories': categories,
        'selected_category': selected_category,
    })


def events_detail(request, slug):
    event = Event.objects.filter(slug=slug).first()
    if not event:
        raise Http404('Event not found')
    related_events = Event.objects.exclude(slug=slug).order_by('-event_date')[:3]
    return render(request, 'core/events_detail.html', {'event': event, 'related_events': related_events})


def all_events(request):
    from .models import Category
    search_query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '').strip()
    now = timezone.now()
    upcoming_events = Event.objects.filter(event_date__gte=now).order_by('event_date')
    past_events = Event.objects.filter(event_date__lt=now).order_by('-event_date')

    if selected_category:
        upcoming_events = upcoming_events.filter(category__name__iexact=selected_category)
        past_events = past_events.filter(category__name__iexact=selected_category)

    if search_query:
        search_filter = Q(
            title_en__icontains=search_query
        ) | Q(
            description_en__icontains=search_query
        ) | Q(
            venue__icontains=search_query
        ) | Q(
            category__name__icontains=search_query
        )
        upcoming_events = upcoming_events.filter(search_filter)
        past_events = past_events.filter(search_filter)

    categories = Category.objects.all()

    tab = request.GET.get('tab', 'upcoming')
    return render(request, 'core/all_events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'categories': categories,
        'selected_category': selected_category,
        'active_tab': tab if tab in ['upcoming', 'past'] else 'upcoming',
    })


def talent(request):
    talents = Talent.objects.all().order_by('-created_at')
    return render(request, 'core/talent.html', {'talents': talents})


def talent_detail(request, slug):
    talent_obj = Talent.objects.filter(slug=slug).first()
    if not talent_obj:
        raise Http404('Talent not found')
    related_talents = Talent.objects.exclude(slug=slug)[:3]
    return render(request, 'core/talent_detail.html', {'talent': talent_obj, 'related_talents': related_talents})


def partnerships(request):
    return render(request, 'core/partnerships.html')


def media_gallery(request):
    from .models import Category
    search_query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '').strip()
    media_items = Gallery.objects.all().order_by('-created_at')

    if selected_category:
        media_items = media_items.filter(category__name__iexact=selected_category)

    if search_query:
        media_items = media_items.filter(
            Q(title__icontains=search_query) | Q(category__name__icontains=search_query)
        )

    photos = media_items.filter(Q(video_url='') | Q(video_url__isnull=True)).order_by('-created_at')
    videos = media_items.exclude(Q(video_url='') | Q(video_url__isnull=True)).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'all_media': media_items,
        'photos': photos,
        'videos': videos,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
    }
    return render(request, 'core/media_gallery.html', context)


def blog(request):
    from .models import Category
    posts = Blog.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    limited_posts = posts[:4]
    has_more_posts = posts.count() > 4
    return render(request, 'core/blog.html', {
        'page_obj': limited_posts,
        'posts': limited_posts,
        'categories': categories,
        'has_more_posts': has_more_posts,
        'show_all': False,
    })


def blog_all(request):
    from .models import Category
    posts = Blog.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'core/blog.html', {
        'page_obj': posts,
        'posts': posts,
        'categories': categories,
        'has_more_posts': False,
        'show_all': True,
    })


def blog_detail(request, slug):
    post = Blog.objects.filter(slug=slug).first()
    if not post:
        raise Http404('Blog post not found')
    related = Blog.objects.exclude(slug=slug).order_by('-created_at')[:3]
    return render(request, 'core/blog_detail.html', {'post': post, 'related_posts': related})


def news(request):
    return redirect('blog')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you. Your message has been received. We will get back to you shortly!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
