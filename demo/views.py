from django.http import HttpResponse


def index(request):
    """index method rendes index view.

        Args:
            request: request object

        Returns:
            Outputs html response.

        """
    return HttpResponse("Hey Dude - you did it - you managed to run demo2 branch!! "
                        " Once again, greatings from Symphony Crew!")
