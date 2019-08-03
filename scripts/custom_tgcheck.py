	#Owner: Torrance Gordon
	#date: 8/2/2019
	#Description: Script to to create random data for datadog metric and monitoring.
	#requires datadog agent and python installed.
	
	# the following try/except block will make the custom check compatible with any Agent version
	try:
	    # first, try to import the base class from old versions of the Agent...
	    from checks import AgentCheck
	    import random
	except ImportError:
	    # ...if the above failed, the check is running in Agent version 6 or later
	    from datadog_checks.checks import AgentCheck
	
	# content of the special variable __version__ will be shown in the Agent status page
	__version__ = "1.0.0"
	
	
	#this class will generate a random number from python and use datadog function to send data points to datadog
	class tgcheck(AgentCheck):
	    def check(self, instance):
	        my_metric = random.randint(1,1001)
	        self.gauge('mymetric.sending', my_metric, tags=['tgname:custom_tgcheck'])
#################################################