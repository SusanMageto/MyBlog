
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from App import db
from App.main.forms import CommentForm
from App.models import Post,Comment
from App.posts.forms import PostForm
from App.posts.utils import save_picture
posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])

def new_post():
    form = PostForm()
    posts = Post.query.order_by(Post.date_posted.desc())
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Blog has been created!', 'success')
        return redirect(url_for('posts.new_post'))
    
    return render_template('create_post.html', title='New Post',
                           form=form,posts=posts)

@posts.route("/post/<int:post_id>",methods=['GET','POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comment = Comment.query.filter_by(post_id=post_id).all()

    form = CommentForm()

    if request.method == 'POST':
        if form.validate_on_submit():

            comment = Comment(comment=form.comment.data,post_id=post_id)
            db.session.add(comment)
            flash('Your comment has been submited','success')
            db.session.commit()
            return redirect(request.url)
    return render_template('post.html', title=post.title, post=post,comment=comment,form=form)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/<int:comment_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id,comment_id):
    post = Post.query.get_or_404(post_id)
    comment = Comment.query.get_or_404(comment_id)

    if post.author!= current_user:
        abort(403)
    db.session.delete(post)
    db.session.delete(comment)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))




         








