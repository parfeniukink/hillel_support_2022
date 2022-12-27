from django.http import JsonResponse
from exchange_rates.services import ExchangeRatesService
from exchange_rates.domain import (
    ExchangeRatesServiceRequest,
    ExchangeRatesServiceResponse,
)


def convert(request):
    from_currency = "USD"
    to_currency = "EUR"

    exchage_rates_service = ExchangeRatesService(
        request=ExchangeRatesServiceRequest(
            from_currency=from_currency,
            to_currency=to_currency,
        )
    )

    result: ExchangeRatesServiceResponse = exchage_rates_service.convert()
    return JsonResponse(result.dict())
