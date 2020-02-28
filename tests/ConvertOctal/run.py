from pysys.constants import *
from apamax.analyticsbuilder.basetest import AnalyticsBuilderBaseTest
 
 
class PySysTest(AnalyticsBuilderBaseTest):
    def execute(self):
        correlator = self.startAnalyticsBuilderCorrelator(
            blockSourceDir=f'{self.project.TEST_SUBJECT_DIR}/blocks')
        self.createTestModel('apamax.analyticsbuilder.BaseNConverter')
        self.sendEventStrings(correlator,
                              self.timestamp(1),
                              self.inputEvent('input', "103"),
                              self.timestamp(2),
                              self.inputEvent('input', "123"),
                              self.timestamp(5),
                              )
 
    def validate(self):
        self.assertGrep('output.evt', expr=self.outputExpr('numericConversion', 67))
        self.assertGrep('output.evt', expr=self.outputExpr('numericConversion', 83))