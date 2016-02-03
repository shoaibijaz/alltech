from django.views.generic import TemplateView, View,ListView


class HomeView(TemplateView):
    template_name = "public/home.html"

    def get(self, request, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

class Home2View(TemplateView):
    template_name = "public/home2.html"

    def get(self, request, *args, **kwargs):
        context = super(Home2View, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(Home2View, self).dispatch(*args, **kwargs)

class AboutView(TemplateView):
    template_name = "public/about.html"

    def get(self, request, *args, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(AboutView, self).dispatch(*args, **kwargs)

class ContactView(TemplateView):
    template_name = "public/contact.html"

    def get(self, request, *args, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ContactView, self).dispatch(*args, **kwargs)

class ProjectView(TemplateView):
    template_name = "public/projects.html"

    def get(self, request, *args, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ProjectView, self).dispatch(*args, **kwargs)

class Project2ColView(TemplateView):
    template_name = "public/projects_2col.html"

    def get(self, request, *args, **kwargs):
        context = super(Project2ColView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(Project2ColView, self).dispatch(*args, **kwargs)

class ProjectSingleView(TemplateView):
    template_name = "public/project_single.html"

    def get(self, request, *args, **kwargs):
        context = super(ProjectSingleView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ProjectSingleView, self).dispatch(*args, **kwargs)


class ConstructionView(TemplateView):
    template_name = "public/construction.html"

    def get(self, request, *args, **kwargs):
        context = super(ConstructionView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ConstructionView, self).dispatch(*args, **kwargs)

class ServicesView(TemplateView):
    template_name = "public/services.html"

    def get(self, request, *args, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ServicesView, self).dispatch(*args, **kwargs)

class BuildingView(TemplateView):
    template_name = "public/building.html"

    def get(self, request, *args, **kwargs):
        context = super(BuildingView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(BuildingView, self).dispatch(*args, **kwargs)

class IsolationView(TemplateView):
    template_name = "public/isolation.html"

    def get(self, request, *args, **kwargs):
        context = super(IsolationView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(IsolationView, self).dispatch(*args, **kwargs)

class PaintingView(TemplateView):
    template_name = "public/painting.html"

    def get(self, request, *args, **kwargs):
        context = super(PaintingView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(PaintingView, self).dispatch(*args, **kwargs)

class ElectricyView(TemplateView):
    template_name = "public/electricy.html"

    def get(self, request, *args, **kwargs):
        context = super(ElectricyView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ElectricyView, self).dispatch(*args, **kwargs)

class ProjectingView(TemplateView):
    template_name = "public/projecting.html"

    def get(self, request, *args, **kwargs):
        context = super(ProjectingView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ProjectingView, self).dispatch(*args, **kwargs)


class BlogView(TemplateView):
    template_name = "public/blog.html"

    def get(self, request, *args, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(BlogView, self).dispatch(*args, **kwargs)

class SinglePostView(TemplateView):
    template_name = "public/single_post.html"

    def get(self, request, *args, **kwargs):
        context = super(SinglePostView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(SinglePostView, self).dispatch(*args, **kwargs)

class ErrorView(TemplateView):
    template_name = "public/404_error.html"

    def get(self, request, *args, **kwargs):
        context = super(ErrorView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ErrorView, self).dispatch(*args, **kwargs)