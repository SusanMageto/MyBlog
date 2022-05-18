
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired





class CommentForm(FlaskForm):
    comment = TextAreaField('Comment...', validators=[DataRequired()])
    submit = SubmitField('comment')