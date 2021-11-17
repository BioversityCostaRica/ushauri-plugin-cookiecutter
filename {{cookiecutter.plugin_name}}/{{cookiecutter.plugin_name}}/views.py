from ushauri.plugins.utilities import ushauriPublicView, ushauriPrivateView


class MyPublicView(ushauriPublicView):
    def processView(self):
        return {}


class MyPrivateView(ushauriPrivateView):
    def processView(self):
        return {"message": self._("Just a message from the plugin")}
