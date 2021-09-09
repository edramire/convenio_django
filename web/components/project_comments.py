from django_unicorn.components import UnicornView
from web.models import Comment

class ProjectCommentsView(UnicornView):
    comments = []
    project_id = 0
    comment_text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self.project_id = kwargs.get("project_id")
        self.comments = Comment.objects.filter(project__pk=self.project_id)

    def submit_comment(self):
        user_id = self.request.user.id
        newComment = Comment.objects.create(comment=self.comment_text, project_id=self.project_id, user_id=user_id)
        self.comments = Comment.objects.filter(project__pk=self.project_id)
        self.comment_text = ""
