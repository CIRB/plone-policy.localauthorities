from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyLocalauthorities(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.localauthorities
        xmlconfig.file('configure.zcml',
                       policy.localauthorities,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.localauthorities:default')

POLICY_LOCALAUTHORITIES_FIXTURE = PolicyLocalauthorities()
POLICY_LOCALAUTHORITIES_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_LOCALAUTHORITIES_FIXTURE, ),
                       name="PolicyLocalauthorities:Integration")