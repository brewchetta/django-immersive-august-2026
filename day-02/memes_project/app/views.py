from django.shortcuts import render

youtube_embeds = [
    "7FwDP17XPlk?si=XJvyQZJm0zmHNi8R",
    "hvL1339luv0?si=HO-58Q1pg9DfM3KV",
    "RrESvSRNpeo?si=D1fIAJxd3jocqMdw",
    "BrgPzp0GBcw?si=lPVzPPTVrH_Y-66f"
]

def home(request):
    context = {
        "youtube_embeds": youtube_embeds
    }
    return render(request, 'app/home.html', context)