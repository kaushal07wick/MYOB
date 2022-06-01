from flask import render_template, request, Blueprint
from newsapi import NewsApiClient
from blog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)

    newsapi = NewsApiClient(api_key="12692f50f97a481cb516c2d540b6dc15")
    topheadlines = newsapi.get_top_headlines(sources="google-news-in,the-verge,bbc-news,wired,business-insider,google-news", page_size=10)
 
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
 
    mylist = zip(news, desc, img)
 
    return render_template('blog.html', context = mylist, posts=posts)
 

@main.route("/about")
def about():
    return render_template('about.html', title='About')

