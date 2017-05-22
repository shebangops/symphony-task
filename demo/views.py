from django.http import HttpResponse


def index(request):
    """index method rendes index view.

        Args:
            request: request object

        Returns:
            Outputs html response.

        """
    return HttpResponse("Hey Dude - you did it, greatings from Symphony Crew!")
