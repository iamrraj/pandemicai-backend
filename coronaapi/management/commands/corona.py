from django.core.management.base import BaseCommand
import requests
from coronaapi.models import CoronaAge, CoronaSex, CoronaComorbidity, Hackathon, Area, Total


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = 'https://api.the2019ncov.com/api/fatality-rate'
        r = requests.get(url)
        titles = r.json()
        print(titles)


# corona_ages = CoronaAge.objects.all()
# new_ages = []
# existing_ages = []
# for title in titles['byAge'] or []:
#     entry = corona_ages.filter(age=title['age']).first():
#     if not entry:
#         new_data = CoronaAge(**title)
#         new_ages.append(new_data)
#     else:
#         entry['age'] = title['age']
#         entry['rate'] = title['rate']
#         existing_ages.append(new_date)

# CoronaAge.objects.bulk_create(new_ages)
# CoronaAge.objects.bulk_update(existing_ages)
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


# Only for country and proviences
        url1 = 'http://covid19api.xapix.io/v2/locations'
        r = requests.get(url1)
        corona = r.json()

        for hack in corona['locations'] or []:
            Hackathon.objects.update_or_create(
                lat=hack['coordinates']['latitude'],
                long=hack['coordinates']['longitude'],
                country=hack['country'],
                country_code=hack['country_code'],
                totalConfirmed=hack['latest']['confirmed'],
                totalDeaths=hack['latest']['deaths'],
                totalRecovered=hack['latest']['recovered'],
                province=hack['province'],
                defaults={
                    'country': hack['country'], 'country_code': hack['country_code']},
            )


# Only for country and proviences  microsoftdata
        url1 = 'https://www.bing.com/covid/data?IG=77591E68DA4B43C5B2656E9D33E5AAB8'
        r = requests.get(url1)
        corona = r.json()

        for micro in corona['areas'] or []:
            Area.objects.update_or_create(
                lat=micro['lat'],
                long=micro['long'],
                country=micro['country'],
                displayName=micro['displayName'],
                main_id=micro['id'],
                totalConfirmed=micro['totalConfirmed'],
                totalDeaths=micro['totalDeaths'],
                totalRecovered=micro['totalRecovered'],
                defaults={
                    'country': micro['country'], 'displayName': micro['displayName'], 'main_id': micro['id']},
            )


# total Cases overall
        # for microo in corona or []:
        #     Total.objects.update_or_create(
        #         totalConfirmed=microo['totalConfirmed'],
        #         totalDeaths=microo['totalDeaths'],
        #         totalRecovered=microo['totalRecovered'],
        #         defaults={
        #             'totalConfirmed': microo['totalConfirmed'], 'totalDeaths': microo['totalDeaths'], 'totalRecovered': microo['totalRecovered']},
        #     )
