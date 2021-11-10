from ushauri.plugins.utilities import ushauriPublicView, ushauriPrivateView


class MyPublicView(ushauriPublicView):
    def process_view(self):
        return {}


class MyPrivateView(ushauriPrivateView):
    def process_view(self):
        return {"message": self._("Just a message from the plugin")}
