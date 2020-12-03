#
#  $Copyright (c) 2019 Software AG, Darmstadt, Germany and/or Software AG USA Inc., Reston, VA, USA, and/or its subsidiaries and/or its affiliates and/or their licensors.$
#   This file is licensed under the Apache 2.0 license - see https://www.apache.org/licenses/LICENSE-2.0
#

from pysys.constants import *
from apamax.analyticsbuilder.basetest import AnalyticsBuilderBaseTest

class PySysTest(AnalyticsBuilderBaseTest):
	def execute(self):
		correlator = self.startAnalyticsBuilderCorrelator(blockSourceDir=f'{self.project.SOURCE}/blocks/')
		
		# engine_receive process listening on all the channels.
		correlator.receive('all.evt')
		
		# Deploying a new model with correct parameter.
		self.modelId = self.createTestModel('apamax.analyticsbuilder.custom.TimeAtLevelCounting', {'threshold':-30.0})
		
		self.sendEventStrings(correlator,
		                      self.timestamp(1582902000),
		                      self.inputEvent('value', -20, id = self.modelId),
		                      self.timestamp(1582903000),
		                      self.inputEvent('value', -29.9, id = self.modelId),
		                      self.timestamp(1582903010),
		                      self.inputEvent('value', -32.0, id = self.modelId),
		                      self.timestamp(1582903910),
		                      self.inputEvent('value', -70.0, id = self.modelId),
		                      self.timestamp(1582904000),
							  self.inputEvent('value',-30.0, id = self.modelId),
							  self.timestamp(1582904500),
							  self.inputEvent('value', -19.99, id = self.modelId),
		                      self.timestamp(1582905000),
							   self.inputEvent('value', 47.00, id = self.modelId),
		                      self.timestamp(1582905200),
							   self.inputEvent('value', -35.2, id = self.modelId),
		                      self.timestamp(1582906000),
							  self.inputEvent('value', -50.6, id = self.modelId),
		                      self.timestamp(1582907000),
							  )

	def validate(self):

		self.assertGrep(self.analyticsBuilderCorrelator.logfile, expr='Model \"' + self.modelId + '\" with PRODUCTION mode has started')
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',0,self.modelId,"",1582902000.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',0,self.modelId,"",1582903000.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',0,self.modelId,"",1582903010.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',900,self.modelId,"",1582903910.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',990,self.modelId,"",1582904000.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',0,self.modelId,"",1582904500.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',0,self.modelId,"",1582905000.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',0,self.modelId,"",1582905200.1,{}))
		self.assertGrep('output.evt', expr=self.outputExpr('timeAtLevelOutput',800,self.modelId,"",1582906000.1,{}))