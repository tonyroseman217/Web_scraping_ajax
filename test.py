import requests
import json
import html2text
URL = "https://www.accenture.com/sg-en/careers/jobsearch?jk=Technology&sb=0&vw=1&is_rj=0&pg=1"
params = URL.split("?")[1].split("&")

paramdata = {}
paramdata['startIndex'] = int(params[4].split("=")[1])-1
paramdata['maxResultSize'] = 15
paramdata['jobKeyword'] = params[0].split("=")[1]
paramdata['jobLanguage'] = 'en'
paramdata['countrySite'] = 'sg-en'
paramdata['sortBy'] = params[1].split("=")[1]
paramdata['aggregations'] = '[{"fieldName":"location"},{"fieldName":"postedDate"},{"fieldName":"jobTypeDescription"},{"fieldName":"workforceEntity"},{"fieldName":"businessArea"},{"fieldName":"skill"},{"fieldName":"travelPercentage"},{"fieldName":"yearsOfExperience"},{"fieldName":"specialization"}]'
paramdata['jobCountry'] = 'Singapore,Vietnam'
paramdata['componentId'] = 'careerjobsearchresults-001'
paramdata['jobFilters'] = '[]'
# paramdata['startIndex'] = 0

resp = requests.post('https://www.accenture.com/api/accenture/jobsearch/result', data=paramdata)
jobs_obj = json.loads(resp.text)
print(len(jobs_obj['data']))
count = 0
for job in jobs_obj['data']:
    count+=1
    print(str(count) + " : " + job['title'])
    print("url" + " : " + job['jobDetailUrl'])
    print(job['skill'])
    print(html2text.html2text(job['jobDescription']))
    print("-----------------------------------------------------------------------------------------------------------------------")
    print()

