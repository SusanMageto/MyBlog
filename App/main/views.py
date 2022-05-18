
from crypt import methods
from flask import render_template, request, Blueprint,flash,redirect,url_for
from App.models import Post,Comment
from App.main.forms import CommentForm
from App import db
import requests
import json

main = Blueprint('main', __name__)


@main.route("/",methods=['GET','POST'])
@main.route("/home",methods=['GET','POST'])
def home():
    r = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
   
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

   

    comment = Comment.query.order_by(Comment.id.desc())
    # add coment 
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            comment = Comment(comment=form.comment.data)
            db.session.add(comment)
            db.session.commit()
            flash('Comment was added','success')
            return redirect(url_for('main.home'))
    return render_template('home.html', posts=posts,comment=comment,form=form,qoutes=json.loads(r.text)['quote'],author=json.loads(r.text)['author'])


@main.route("/about")
def about():
    return render_template('about.html', title='About')