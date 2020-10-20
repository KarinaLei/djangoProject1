from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course

# Create your views here.

# demonstrate Mixin:
# to extend class views with some new code

class CourseObjectMixin(object):
    model = Course
    lookup = 'id'

    # now, this block of code can replace all of the redundant get_object() blocks underneath,
    # by simplying inheriting from it by doing: CourseDeleteView(CourseObjectMixin, View)
    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


# to demonstrate how to convert between raw class-based view & function-based view (and vice versa)
# you usually would want to use class-based views because of the benefits of inheritance.
# this is to demonstrate RAW class-based views inheriting from Views.
# the other examples that we did previously used the Generic Views.

class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('/courses/')
        return render(request, self.template_name, context)


class CourseUpdateView(View):
    template_name = 'courses/course_create.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request, *args, **kwargs):
        # GET method
        form = CourseModelForm()    # this doesn't actually do anything, becuase
                                    # course_create.html only accepts POST method
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        # now, save the form!
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


# here, you can easily create a subclass of the super class, and if you use this class instead in urls.py,
# everything will render correctly
class FilteredCourseListView(CourseListView):
    queryset = Course.objects.filter(id=1)


class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {})


# HTTP method
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})