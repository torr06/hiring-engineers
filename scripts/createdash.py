from datadog import initialize, api

options = {
    'api_key': '03f8bbb2ad4e26d71f155619f43721a4',
    'app_key': '13c837ff4046341d52e41aac48204698e837e3f3'
}

initialize(**options)


title = "Torrance Handy Dandy Dashboard"


widgets = [
    {
        "definition": {
            "type": "timeseries",
            "requests": [
                {
                   "q": "anomalies(avg:mongodb.dur.commits{*}, 'basic', 2)"
                }
                
            ],
            "title": "dur.commits"
        }
    },
    {
        "definition": {
            "type": "timeseries",
            "requests": [
                {
                    "q": "avg:mymetric.sending{*}.rollup(avg, 60)"
                }
            ],
            "title": "mymetric.sending"
        }
    }

]
layout_type = "ordered"
description = "Display dur commit anomalies and a rolled up mymetric"
is_read_only = True
notify_list = [
    "tlgordon06@gmail.com"
]
template_variables = [
    {
        "name": "ddtestvm1",
        "prefix": "host",
        "default": "myhost"
    }
]
     
api.Dashboard.create(title=title,
                     widgets=widgets,
                     layout_type=layout_type,
                     description=description,
                     is_read_only=is_read_only,
                     notify_list=notify_list,
                     template_variables=template_variables)