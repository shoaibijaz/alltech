from django.views.generic import TemplateView, View,ListView


class HomeView(TemplateView):
    template_name = "public/home.html"

    def get(self, request, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

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

class HostingView(TemplateView):
    template_name = "public/hosting.html"

    def get(self, request, *args, **kwargs):
        context = super(HostingView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(HostingView, self).dispatch(*args, **kwargs)


class CloudView(TemplateView):
    template_name = "public/cloud.html"

    def get(self, request, *args, **kwargs):
        context = super(CloudView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(CloudView, self).dispatch(*args, **kwargs)


class ServicesView(TemplateView):
    template_name = "public/services.html"

    def get(self, request, *args, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(ServicesView, self).dispatch(*args, **kwargs)

class PortfolioView(TemplateView):
    template_name = "public/portfolio.html"

    def get(self, request, *args, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, *args, **kwargs):
        return super(PortfolioView, self).dispatch(*args, **kwargs)