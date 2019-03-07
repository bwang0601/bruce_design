from tethys_sdk.base import TethysAppBase, url_map_maker


class BruceDesign(TethysAppBase):
    """
    Tethys app class for bruce design.
    """

    name = 'bruce design'
    index = 'bruce_design:home'
    icon = 'bruce_design/images/icon.gif'
    package = 'bruce_design'
    root_url = 'bruce-design'
    color = '#FFD700'
    description = 'term project'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='home',
                controller='bruce_design.controllers.home'
            ),
            UrlMap(
                name='proposal',
                url='proposal',
                controller='bruce_design.controllers.proposal'
            ),
            UrlMap(
                name='wireframe',
                url='wireframe',
                controller='bruce_design.controllers.wireframe'
            ),
        )

        return url_maps
