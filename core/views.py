from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ContactForm


BLOG_POSTS = [
    {
        'slug': 'creative-spaces-matter',
        'title': 'Why Creative Spaces Matter for Youth Development',
        'excerpt': 'Creative hubs build confidence, discipline, belonging, and clear pathways to real opportunity for young people.',
        'category': 'Youth Development',
        'cover_image': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=900&q=80',
        'thumb_image': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&q=80',
        'read_time': 5,
        'author_name': 'ISONGA Team',
        'published_date': 'May 10, 2025',
        'tags': ['Youth', 'Creative Space', 'Empowerment', 'Rwanda'],
    },
    {
        'slug': 'talent-showcase-highlights',
        'title': 'Highlights from Our Latest Talent Showcase',
        'excerpt': 'A look back at performance energy, audience engagement, and the creative growth on display during our most recent showcase night in Musanze.',
        'category': 'Talent',
        'thumb_image': 'https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=600&q=80',
        'read_time': 3,
        'author_name': 'ISONGA Team',
        'published_date': 'Apr 28, 2025',
        'tags': ['Talent', 'Performance'],
    },
    {
        'slug': 'musanze-creative-destination',
        'title': 'Building Musanze as a Creative and Cultural Destination',
        'excerpt': 'How events and youth participation can strengthen regional cultural identity and put Musanze on Rwanda\'s creative map for good.',
        'category': 'Culture',
        'thumb_image': 'https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=600&q=80',
        'read_time': 6,
        'author_name': 'ISONGA Team',
        'published_date': 'Apr 14, 2025',
        'tags': ['Culture', 'Community'],
    },
    {
        'slug': 'youth-stage-opportunity',
        'title': 'Giving Young People a Stage Before the World Gives Them a Chance',
        'excerpt': 'Why early performance opportunities shape more than skill — they build the resilience needed for a lasting creative career.',
        'category': 'Youth',
        'thumb_image': 'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&q=80',
        'read_time': 4,
        'author_name': 'ISONGA Team',
        'published_date': 'Apr 5, 2025',
        'tags': ['Youth', 'Opportunity'],
    },
    {
        'slug': 'digital-skills-creative-economy',
        'title': 'Why Digital Skills Are Non-Negotiable for Today\'s Creative Economy',
        'excerpt': 'From social media to content production, the creative industry has gone fully digital — and ISONGA is preparing youth for that reality.',
        'category': 'Insights',
        'thumb_image': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&q=80',
        'read_time': 5,
        'author_name': 'ISONGA Team',
        'published_date': 'Mar 22, 2025',
        'tags': ['Digital Skills', 'Future'],
    },
    {
        'slug': 'isonga-community-hub',
        'title': 'ISONGA and the Wider Community: Why This Hub Belongs to Everyone',
        'excerpt': 'From local families to partner organisations, ISONGA Centre is woven into the creative and social fabric of Musanze.',
        'category': 'Community',
        'thumb_image': 'https://images.unsplash.com/photo-1529390079861-591de354faf5?w=600&q=80',
        'read_time': 4,
        'author_name': 'ISONGA Team',
        'published_date': 'Feb 28, 2025',
        'tags': ['Community', 'Impact'],
    },
]


def home(request):
    context = {
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


def events(request):
    return render(request, 'core/events.html')


def talent(request):
    return render(request, 'core/talent.html')


def partnerships(request):
    return render(request, 'core/partnerships.html')


def media_gallery(request):
    return render(request, 'core/media_gallery.html')


def blog(request):
    return render(request, 'core/blog.html', {'posts': BLOG_POSTS})


def blog_detail(request, slug):
    post = next((p for p in BLOG_POSTS if p['slug'] == slug), None)
    if not post:
        raise Http404('Blog post not found')
    related = [p for p in BLOG_POSTS if p['slug'] != slug][:3]
    return render(request, 'core/blog_detail.html', {'post': post, 'related_posts': related})


def news(request):
    return redirect('blog')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you. Your message has been received.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
