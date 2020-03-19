from django.core.management.base import BaseCommand
import requests
from demo.models import CoronaAge, CoronaSex, CoronaComorbidity


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = 'https://api.the2019ncov.com/api/fatality-rate'
        r = requests.get(url)
        titles = r.json()
        print(titles)

# For between age.
        for agee in titles['byAge'] or []:
            CoronaAge.objects.update_or_create(
                age=agee['age'],
                rate=agee['rate'],
                defaults={'age': agee['age'], 'rate': agee['rate']},
            )
        # context = {'titles': CoronaAge.objects.all()}


# For sex male or female
        for sex in titles['bySex'] or []:
            CoronaSex.objects.update_or_create(
                sex=sex['sex'],
                rate=sex['rate'],
                defaults={'sex': sex['sex'], 'rate': sex['rate']},
            )
        # context = {'titles': CoronaSex.objects.all()}

# For comorbidity
        for comorbidity in titles['byComorbidity'] or []:
            CoronaComorbidity.objects.update_or_create(
                condition=comorbidity['preExistingCondition'],
                rate=comorbidity['rate'],
                defaults={
                    'condition': comorbidity['preExistingCondition'], 'rate': comorbidity['rate']},
            )

        # context = {'titles': CoronaComorbidity.objects.all()}
