__author__ = 'vitor'

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from django.db import IntegrityError
from core.forms import TaskForm
from core.models import Task


class HomeTest(TestCase):

	def setUp(self):
		self.resp = self.client.get(r('home'))

	def test_get(self):
		self.assertEqual(200, self.resp.status_code)

	def test_html(self):
		self.assertTemplateUsed(self.resp, 'index.html')

	def test_form_context(self):
		form = self.resp.context['form']
		self.assertIsInstance(form, TaskForm)

	def test_html_form(self):
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 4)


class TaskTest(TestCase):

	def setUp(self):
		data = dict(name='Task teste 1', is_done=False)
		self.resp = self.client.post(r('add_task'), data)

	def test_post(self):
		self.assertEqual(302, self.resp.status_code)

	def test_save(self):
		self.assertTrue(Task.objects.exists())


class TaskPostFailTest(TestCase):

	def setUp(self):
		data = dict(is_done=False)
		self.resp = self.client.post(r('add_task'), data)

	def test_post(self):
		self.assertEqual(200, self.resp.status_code)

	def test_form_errors(self):
		self.assertTrue(self.resp.context['form'].errors)

	def test_not_save(self):
		self.assertFalse(Task.objects.exists())


class TaskModelTest(TestCase):

	def setUp(self):
		self.obj = Task(name='Task teste 1', is_done=False)

	def test_create(self):
		self.obj.save()
		self.assertEqual(1, self.obj.pk)