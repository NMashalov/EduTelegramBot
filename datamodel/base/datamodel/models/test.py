from django.db import models

class Test(models.Model):
    question = models.TextField()


class UserResponse(models.Model):
	'''User response to a single question.'''
	quiz_instance = models.ForeignKey(QuizInstance)
	question = models.ForeignKey(MultipleChoice)
	response = models.ManyToManyField(MultipleChoiceAnswer, related_name="response")
	time_taken = models.DateTimeField(_('When was the question posed'), auto_now_add=True)
	time_taken_delta = models.DateTimeField(_('When was the question answered'), blank=True)

	def __unicode__(self):
		return u"Response to %s for %s" % (self.question, self.quiz_instance)
	@property
	def is_correct(self):
		return self.question.correct_answer.all()==self.response.all()