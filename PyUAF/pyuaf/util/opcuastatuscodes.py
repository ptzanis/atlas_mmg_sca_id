# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_opcuastatuscodes', [dirname(__file__)])
        except ImportError:
            import _opcuastatuscodes
            return _opcuastatuscodes
        if fp is not None:
            try:
                _mod = imp.load_module('_opcuastatuscodes', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _opcuastatuscodes = swig_import_helper()
    del swig_import_helper
else:
    import _opcuastatuscodes
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _opcuastatuscodes.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _opcuastatuscodes.SwigPyIterator_value(self)
    def incr(self, n=1): return _opcuastatuscodes.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _opcuastatuscodes.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _opcuastatuscodes.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _opcuastatuscodes.SwigPyIterator_equal(self, *args)
    def copy(self): return _opcuastatuscodes.SwigPyIterator_copy(self)
    def next(self): return _opcuastatuscodes.SwigPyIterator_next(self)
    def __next__(self): return _opcuastatuscodes.SwigPyIterator___next__(self)
    def previous(self): return _opcuastatuscodes.SwigPyIterator_previous(self)
    def advance(self, *args): return _opcuastatuscodes.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _opcuastatuscodes.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _opcuastatuscodes.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _opcuastatuscodes.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _opcuastatuscodes.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _opcuastatuscodes.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _opcuastatuscodes.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _opcuastatuscodes.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

_OpcUa_StatusCodes_H_ = _opcuastatuscodes._OpcUa_StatusCodes_H_
OpcUa_BadUnexpectedError = _opcuastatuscodes.OpcUa_BadUnexpectedError
OpcUa_BadInternalError = _opcuastatuscodes.OpcUa_BadInternalError
OpcUa_BadOutOfMemory = _opcuastatuscodes.OpcUa_BadOutOfMemory
OpcUa_BadResourceUnavailable = _opcuastatuscodes.OpcUa_BadResourceUnavailable
OpcUa_BadCommunicationError = _opcuastatuscodes.OpcUa_BadCommunicationError
OpcUa_BadEncodingError = _opcuastatuscodes.OpcUa_BadEncodingError
OpcUa_BadDecodingError = _opcuastatuscodes.OpcUa_BadDecodingError
OpcUa_BadEncodingLimitsExceeded = _opcuastatuscodes.OpcUa_BadEncodingLimitsExceeded
OpcUa_BadRequestTooLarge = _opcuastatuscodes.OpcUa_BadRequestTooLarge
OpcUa_BadResponseTooLarge = _opcuastatuscodes.OpcUa_BadResponseTooLarge
OpcUa_BadUnknownResponse = _opcuastatuscodes.OpcUa_BadUnknownResponse
OpcUa_BadTimeout = _opcuastatuscodes.OpcUa_BadTimeout
OpcUa_BadServiceUnsupported = _opcuastatuscodes.OpcUa_BadServiceUnsupported
OpcUa_BadShutdown = _opcuastatuscodes.OpcUa_BadShutdown
OpcUa_BadServerNotConnected = _opcuastatuscodes.OpcUa_BadServerNotConnected
OpcUa_BadServerHalted = _opcuastatuscodes.OpcUa_BadServerHalted
OpcUa_BadNothingToDo = _opcuastatuscodes.OpcUa_BadNothingToDo
OpcUa_BadTooManyOperations = _opcuastatuscodes.OpcUa_BadTooManyOperations
OpcUa_BadTooManyMonitoredItems = _opcuastatuscodes.OpcUa_BadTooManyMonitoredItems
OpcUa_BadDataTypeIdUnknown = _opcuastatuscodes.OpcUa_BadDataTypeIdUnknown
OpcUa_BadCertificateInvalid = _opcuastatuscodes.OpcUa_BadCertificateInvalid
OpcUa_BadSecurityChecksFailed = _opcuastatuscodes.OpcUa_BadSecurityChecksFailed
OpcUa_BadCertificateTimeInvalid = _opcuastatuscodes.OpcUa_BadCertificateTimeInvalid
OpcUa_BadCertificateIssuerTimeInvalid = _opcuastatuscodes.OpcUa_BadCertificateIssuerTimeInvalid
OpcUa_BadCertificateHostNameInvalid = _opcuastatuscodes.OpcUa_BadCertificateHostNameInvalid
OpcUa_BadCertificateUriInvalid = _opcuastatuscodes.OpcUa_BadCertificateUriInvalid
OpcUa_BadCertificateUseNotAllowed = _opcuastatuscodes.OpcUa_BadCertificateUseNotAllowed
OpcUa_BadCertificateIssuerUseNotAllowed = _opcuastatuscodes.OpcUa_BadCertificateIssuerUseNotAllowed
OpcUa_BadCertificateUntrusted = _opcuastatuscodes.OpcUa_BadCertificateUntrusted
OpcUa_BadCertificateRevocationUnknown = _opcuastatuscodes.OpcUa_BadCertificateRevocationUnknown
OpcUa_BadCertificateIssuerRevocationUnknown = _opcuastatuscodes.OpcUa_BadCertificateIssuerRevocationUnknown
OpcUa_BadCertificateRevoked = _opcuastatuscodes.OpcUa_BadCertificateRevoked
OpcUa_BadCertificateIssuerRevoked = _opcuastatuscodes.OpcUa_BadCertificateIssuerRevoked
OpcUa_BadCertificateChainIncomplete = _opcuastatuscodes.OpcUa_BadCertificateChainIncomplete
OpcUa_BadUserAccessDenied = _opcuastatuscodes.OpcUa_BadUserAccessDenied
OpcUa_BadIdentityTokenInvalid = _opcuastatuscodes.OpcUa_BadIdentityTokenInvalid
OpcUa_BadIdentityTokenRejected = _opcuastatuscodes.OpcUa_BadIdentityTokenRejected
OpcUa_BadSecureChannelIdInvalid = _opcuastatuscodes.OpcUa_BadSecureChannelIdInvalid
OpcUa_BadInvalidTimestamp = _opcuastatuscodes.OpcUa_BadInvalidTimestamp
OpcUa_BadNonceInvalid = _opcuastatuscodes.OpcUa_BadNonceInvalid
OpcUa_BadSessionIdInvalid = _opcuastatuscodes.OpcUa_BadSessionIdInvalid
OpcUa_BadSessionClosed = _opcuastatuscodes.OpcUa_BadSessionClosed
OpcUa_BadSessionNotActivated = _opcuastatuscodes.OpcUa_BadSessionNotActivated
OpcUa_BadSubscriptionIdInvalid = _opcuastatuscodes.OpcUa_BadSubscriptionIdInvalid
OpcUa_BadRequestHeaderInvalid = _opcuastatuscodes.OpcUa_BadRequestHeaderInvalid
OpcUa_BadTimestampsToReturnInvalid = _opcuastatuscodes.OpcUa_BadTimestampsToReturnInvalid
OpcUa_BadRequestCancelledByClient = _opcuastatuscodes.OpcUa_BadRequestCancelledByClient
OpcUa_BadTooManyArguments = _opcuastatuscodes.OpcUa_BadTooManyArguments
OpcUa_BadLicenseExpired = _opcuastatuscodes.OpcUa_BadLicenseExpired
OpcUa_BadLicenseLimitsExceeded = _opcuastatuscodes.OpcUa_BadLicenseLimitsExceeded
OpcUa_BadLicenseNotAvailable = _opcuastatuscodes.OpcUa_BadLicenseNotAvailable
OpcUa_GoodSubscriptionTransferred = _opcuastatuscodes.OpcUa_GoodSubscriptionTransferred
OpcUa_GoodCompletesAsynchronously = _opcuastatuscodes.OpcUa_GoodCompletesAsynchronously
OpcUa_GoodOverload = _opcuastatuscodes.OpcUa_GoodOverload
OpcUa_GoodClamped = _opcuastatuscodes.OpcUa_GoodClamped
OpcUa_BadNoCommunication = _opcuastatuscodes.OpcUa_BadNoCommunication
OpcUa_BadWaitingForInitialData = _opcuastatuscodes.OpcUa_BadWaitingForInitialData
OpcUa_BadNodeIdInvalid = _opcuastatuscodes.OpcUa_BadNodeIdInvalid
OpcUa_BadNodeIdUnknown = _opcuastatuscodes.OpcUa_BadNodeIdUnknown
OpcUa_BadAttributeIdInvalid = _opcuastatuscodes.OpcUa_BadAttributeIdInvalid
OpcUa_BadIndexRangeInvalid = _opcuastatuscodes.OpcUa_BadIndexRangeInvalid
OpcUa_BadIndexRangeNoData = _opcuastatuscodes.OpcUa_BadIndexRangeNoData
OpcUa_BadDataEncodingInvalid = _opcuastatuscodes.OpcUa_BadDataEncodingInvalid
OpcUa_BadDataEncodingUnsupported = _opcuastatuscodes.OpcUa_BadDataEncodingUnsupported
OpcUa_BadNotReadable = _opcuastatuscodes.OpcUa_BadNotReadable
OpcUa_BadNotWritable = _opcuastatuscodes.OpcUa_BadNotWritable
OpcUa_BadOutOfRange = _opcuastatuscodes.OpcUa_BadOutOfRange
OpcUa_BadNotSupported = _opcuastatuscodes.OpcUa_BadNotSupported
OpcUa_BadNotFound = _opcuastatuscodes.OpcUa_BadNotFound
OpcUa_BadObjectDeleted = _opcuastatuscodes.OpcUa_BadObjectDeleted
OpcUa_BadNotImplemented = _opcuastatuscodes.OpcUa_BadNotImplemented
OpcUa_BadMonitoringModeInvalid = _opcuastatuscodes.OpcUa_BadMonitoringModeInvalid
OpcUa_BadMonitoredItemIdInvalid = _opcuastatuscodes.OpcUa_BadMonitoredItemIdInvalid
OpcUa_BadMonitoredItemFilterInvalid = _opcuastatuscodes.OpcUa_BadMonitoredItemFilterInvalid
OpcUa_BadMonitoredItemFilterUnsupported = _opcuastatuscodes.OpcUa_BadMonitoredItemFilterUnsupported
OpcUa_BadFilterNotAllowed = _opcuastatuscodes.OpcUa_BadFilterNotAllowed
OpcUa_BadStructureMissing = _opcuastatuscodes.OpcUa_BadStructureMissing
OpcUa_BadEventFilterInvalid = _opcuastatuscodes.OpcUa_BadEventFilterInvalid
OpcUa_BadContentFilterInvalid = _opcuastatuscodes.OpcUa_BadContentFilterInvalid
OpcUa_BadFilterOperatorInvalid = _opcuastatuscodes.OpcUa_BadFilterOperatorInvalid
OpcUa_BadFilterOperatorUnsupported = _opcuastatuscodes.OpcUa_BadFilterOperatorUnsupported
OpcUa_BadFilterOperandCountMismatch = _opcuastatuscodes.OpcUa_BadFilterOperandCountMismatch
OpcUa_BadFilterOperandInvalid = _opcuastatuscodes.OpcUa_BadFilterOperandInvalid
OpcUa_BadFilterElementInvalid = _opcuastatuscodes.OpcUa_BadFilterElementInvalid
OpcUa_BadFilterLiteralInvalid = _opcuastatuscodes.OpcUa_BadFilterLiteralInvalid
OpcUa_BadContinuationPointInvalid = _opcuastatuscodes.OpcUa_BadContinuationPointInvalid
OpcUa_BadNoContinuationPoints = _opcuastatuscodes.OpcUa_BadNoContinuationPoints
OpcUa_BadReferenceTypeIdInvalid = _opcuastatuscodes.OpcUa_BadReferenceTypeIdInvalid
OpcUa_BadBrowseDirectionInvalid = _opcuastatuscodes.OpcUa_BadBrowseDirectionInvalid
OpcUa_BadNodeNotInView = _opcuastatuscodes.OpcUa_BadNodeNotInView
OpcUa_BadServerUriInvalid = _opcuastatuscodes.OpcUa_BadServerUriInvalid
OpcUa_BadServerNameMissing = _opcuastatuscodes.OpcUa_BadServerNameMissing
OpcUa_BadDiscoveryUrlMissing = _opcuastatuscodes.OpcUa_BadDiscoveryUrlMissing
OpcUa_BadSempahoreFileMissing = _opcuastatuscodes.OpcUa_BadSempahoreFileMissing
OpcUa_BadRequestTypeInvalid = _opcuastatuscodes.OpcUa_BadRequestTypeInvalid
OpcUa_BadSecurityModeRejected = _opcuastatuscodes.OpcUa_BadSecurityModeRejected
OpcUa_BadSecurityPolicyRejected = _opcuastatuscodes.OpcUa_BadSecurityPolicyRejected
OpcUa_BadTooManySessions = _opcuastatuscodes.OpcUa_BadTooManySessions
OpcUa_BadUserSignatureInvalid = _opcuastatuscodes.OpcUa_BadUserSignatureInvalid
OpcUa_BadApplicationSignatureInvalid = _opcuastatuscodes.OpcUa_BadApplicationSignatureInvalid
OpcUa_BadNoValidCertificates = _opcuastatuscodes.OpcUa_BadNoValidCertificates
OpcUa_BadIdentityChangeNotSupported = _opcuastatuscodes.OpcUa_BadIdentityChangeNotSupported
OpcUa_BadRequestCancelledByRequest = _opcuastatuscodes.OpcUa_BadRequestCancelledByRequest
OpcUa_BadParentNodeIdInvalid = _opcuastatuscodes.OpcUa_BadParentNodeIdInvalid
OpcUa_BadReferenceNotAllowed = _opcuastatuscodes.OpcUa_BadReferenceNotAllowed
OpcUa_BadNodeIdRejected = _opcuastatuscodes.OpcUa_BadNodeIdRejected
OpcUa_BadNodeIdExists = _opcuastatuscodes.OpcUa_BadNodeIdExists
OpcUa_BadNodeClassInvalid = _opcuastatuscodes.OpcUa_BadNodeClassInvalid
OpcUa_BadBrowseNameInvalid = _opcuastatuscodes.OpcUa_BadBrowseNameInvalid
OpcUa_BadBrowseNameDuplicated = _opcuastatuscodes.OpcUa_BadBrowseNameDuplicated
OpcUa_BadNodeAttributesInvalid = _opcuastatuscodes.OpcUa_BadNodeAttributesInvalid
OpcUa_BadTypeDefinitionInvalid = _opcuastatuscodes.OpcUa_BadTypeDefinitionInvalid
OpcUa_BadSourceNodeIdInvalid = _opcuastatuscodes.OpcUa_BadSourceNodeIdInvalid
OpcUa_BadTargetNodeIdInvalid = _opcuastatuscodes.OpcUa_BadTargetNodeIdInvalid
OpcUa_BadDuplicateReferenceNotAllowed = _opcuastatuscodes.OpcUa_BadDuplicateReferenceNotAllowed
OpcUa_BadInvalidSelfReference = _opcuastatuscodes.OpcUa_BadInvalidSelfReference
OpcUa_BadReferenceLocalOnly = _opcuastatuscodes.OpcUa_BadReferenceLocalOnly
OpcUa_BadNoDeleteRights = _opcuastatuscodes.OpcUa_BadNoDeleteRights
OpcUa_UncertainReferenceNotDeleted = _opcuastatuscodes.OpcUa_UncertainReferenceNotDeleted
OpcUa_BadServerIndexInvalid = _opcuastatuscodes.OpcUa_BadServerIndexInvalid
OpcUa_BadViewIdUnknown = _opcuastatuscodes.OpcUa_BadViewIdUnknown
OpcUa_BadViewTimestampInvalid = _opcuastatuscodes.OpcUa_BadViewTimestampInvalid
OpcUa_BadViewParameterMismatch = _opcuastatuscodes.OpcUa_BadViewParameterMismatch
OpcUa_BadViewVersionInvalid = _opcuastatuscodes.OpcUa_BadViewVersionInvalid
OpcUa_UncertainNotAllNodesAvailable = _opcuastatuscodes.OpcUa_UncertainNotAllNodesAvailable
OpcUa_GoodResultsMayBeIncomplete = _opcuastatuscodes.OpcUa_GoodResultsMayBeIncomplete
OpcUa_BadNotTypeDefinition = _opcuastatuscodes.OpcUa_BadNotTypeDefinition
OpcUa_UncertainReferenceOutOfServer = _opcuastatuscodes.OpcUa_UncertainReferenceOutOfServer
OpcUa_BadTooManyMatches = _opcuastatuscodes.OpcUa_BadTooManyMatches
OpcUa_BadQueryTooComplex = _opcuastatuscodes.OpcUa_BadQueryTooComplex
OpcUa_BadNoMatch = _opcuastatuscodes.OpcUa_BadNoMatch
OpcUa_BadMaxAgeInvalid = _opcuastatuscodes.OpcUa_BadMaxAgeInvalid
OpcUa_BadSecurityModeInsufficient = _opcuastatuscodes.OpcUa_BadSecurityModeInsufficient
OpcUa_BadHistoryOperationInvalid = _opcuastatuscodes.OpcUa_BadHistoryOperationInvalid
OpcUa_BadHistoryOperationUnsupported = _opcuastatuscodes.OpcUa_BadHistoryOperationUnsupported
OpcUa_BadInvalidTimestampArgument = _opcuastatuscodes.OpcUa_BadInvalidTimestampArgument
OpcUa_BadWriteNotSupported = _opcuastatuscodes.OpcUa_BadWriteNotSupported
OpcUa_BadTypeMismatch = _opcuastatuscodes.OpcUa_BadTypeMismatch
OpcUa_BadMethodInvalid = _opcuastatuscodes.OpcUa_BadMethodInvalid
OpcUa_BadArgumentsMissing = _opcuastatuscodes.OpcUa_BadArgumentsMissing
OpcUa_BadTooManySubscriptions = _opcuastatuscodes.OpcUa_BadTooManySubscriptions
OpcUa_BadTooManyPublishRequests = _opcuastatuscodes.OpcUa_BadTooManyPublishRequests
OpcUa_BadNoSubscription = _opcuastatuscodes.OpcUa_BadNoSubscription
OpcUa_BadSequenceNumberUnknown = _opcuastatuscodes.OpcUa_BadSequenceNumberUnknown
OpcUa_BadMessageNotAvailable = _opcuastatuscodes.OpcUa_BadMessageNotAvailable
OpcUa_BadInsufficientClientProfile = _opcuastatuscodes.OpcUa_BadInsufficientClientProfile
OpcUa_BadStateNotActive = _opcuastatuscodes.OpcUa_BadStateNotActive
OpcUa_BadTcpServerTooBusy = _opcuastatuscodes.OpcUa_BadTcpServerTooBusy
OpcUa_BadTcpMessageTypeInvalid = _opcuastatuscodes.OpcUa_BadTcpMessageTypeInvalid
OpcUa_BadTcpSecureChannelUnknown = _opcuastatuscodes.OpcUa_BadTcpSecureChannelUnknown
OpcUa_BadTcpMessageTooLarge = _opcuastatuscodes.OpcUa_BadTcpMessageTooLarge
OpcUa_BadTcpNotEnoughResources = _opcuastatuscodes.OpcUa_BadTcpNotEnoughResources
OpcUa_BadTcpInternalError = _opcuastatuscodes.OpcUa_BadTcpInternalError
OpcUa_BadTcpEndpointUrlInvalid = _opcuastatuscodes.OpcUa_BadTcpEndpointUrlInvalid
OpcUa_BadRequestInterrupted = _opcuastatuscodes.OpcUa_BadRequestInterrupted
OpcUa_BadRequestTimeout = _opcuastatuscodes.OpcUa_BadRequestTimeout
OpcUa_BadSecureChannelClosed = _opcuastatuscodes.OpcUa_BadSecureChannelClosed
OpcUa_BadSecureChannelTokenUnknown = _opcuastatuscodes.OpcUa_BadSecureChannelTokenUnknown
OpcUa_BadSequenceNumberInvalid = _opcuastatuscodes.OpcUa_BadSequenceNumberInvalid
OpcUa_BadProtocolVersionUnsupported = _opcuastatuscodes.OpcUa_BadProtocolVersionUnsupported
OpcUa_BadConfigurationError = _opcuastatuscodes.OpcUa_BadConfigurationError
OpcUa_BadNotConnected = _opcuastatuscodes.OpcUa_BadNotConnected
OpcUa_BadDeviceFailure = _opcuastatuscodes.OpcUa_BadDeviceFailure
OpcUa_BadSensorFailure = _opcuastatuscodes.OpcUa_BadSensorFailure
OpcUa_BadOutOfService = _opcuastatuscodes.OpcUa_BadOutOfService
OpcUa_BadDeadbandFilterInvalid = _opcuastatuscodes.OpcUa_BadDeadbandFilterInvalid
OpcUa_UncertainNoCommunicationLastUsableValue = _opcuastatuscodes.OpcUa_UncertainNoCommunicationLastUsableValue
OpcUa_UncertainLastUsableValue = _opcuastatuscodes.OpcUa_UncertainLastUsableValue
OpcUa_UncertainSubstituteValue = _opcuastatuscodes.OpcUa_UncertainSubstituteValue
OpcUa_UncertainInitialValue = _opcuastatuscodes.OpcUa_UncertainInitialValue
OpcUa_UncertainSensorNotAccurate = _opcuastatuscodes.OpcUa_UncertainSensorNotAccurate
OpcUa_UncertainEngineeringUnitsExceeded = _opcuastatuscodes.OpcUa_UncertainEngineeringUnitsExceeded
OpcUa_UncertainSubNormal = _opcuastatuscodes.OpcUa_UncertainSubNormal
OpcUa_GoodLocalOverride = _opcuastatuscodes.OpcUa_GoodLocalOverride
OpcUa_BadRefreshInProgress = _opcuastatuscodes.OpcUa_BadRefreshInProgress
OpcUa_BadConditionAlreadyDisabled = _opcuastatuscodes.OpcUa_BadConditionAlreadyDisabled
OpcUa_BadConditionAlreadyEnabled = _opcuastatuscodes.OpcUa_BadConditionAlreadyEnabled
OpcUa_BadConditionDisabled = _opcuastatuscodes.OpcUa_BadConditionDisabled
OpcUa_BadEventIdUnknown = _opcuastatuscodes.OpcUa_BadEventIdUnknown
OpcUa_BadEventNotAcknowledgeable = _opcuastatuscodes.OpcUa_BadEventNotAcknowledgeable
OpcUa_BadDialogNotActive = _opcuastatuscodes.OpcUa_BadDialogNotActive
OpcUa_BadDialogResponseInvalid = _opcuastatuscodes.OpcUa_BadDialogResponseInvalid
OpcUa_BadConditionBranchAlreadyAcked = _opcuastatuscodes.OpcUa_BadConditionBranchAlreadyAcked
OpcUa_BadConditionBranchAlreadyConfirmed = _opcuastatuscodes.OpcUa_BadConditionBranchAlreadyConfirmed
OpcUa_BadConditionAlreadyShelved = _opcuastatuscodes.OpcUa_BadConditionAlreadyShelved
OpcUa_BadConditionNotShelved = _opcuastatuscodes.OpcUa_BadConditionNotShelved
OpcUa_BadShelvingTimeOutOfRange = _opcuastatuscodes.OpcUa_BadShelvingTimeOutOfRange
OpcUa_BadNoData = _opcuastatuscodes.OpcUa_BadNoData
OpcUa_BadBoundNotFound = _opcuastatuscodes.OpcUa_BadBoundNotFound
OpcUa_BadBoundNotSupported = _opcuastatuscodes.OpcUa_BadBoundNotSupported
OpcUa_BadDataLost = _opcuastatuscodes.OpcUa_BadDataLost
OpcUa_BadDataUnavailable = _opcuastatuscodes.OpcUa_BadDataUnavailable
OpcUa_BadEntryExists = _opcuastatuscodes.OpcUa_BadEntryExists
OpcUa_BadNoEntryExists = _opcuastatuscodes.OpcUa_BadNoEntryExists
OpcUa_BadTimestampNotSupported = _opcuastatuscodes.OpcUa_BadTimestampNotSupported
OpcUa_GoodEntryInserted = _opcuastatuscodes.OpcUa_GoodEntryInserted
OpcUa_GoodEntryReplaced = _opcuastatuscodes.OpcUa_GoodEntryReplaced
OpcUa_UncertainDataSubNormal = _opcuastatuscodes.OpcUa_UncertainDataSubNormal
OpcUa_GoodNoData = _opcuastatuscodes.OpcUa_GoodNoData
OpcUa_GoodMoreData = _opcuastatuscodes.OpcUa_GoodMoreData
OpcUa_BadAggregateListMismatch = _opcuastatuscodes.OpcUa_BadAggregateListMismatch
OpcUa_BadAggregateNotSupported = _opcuastatuscodes.OpcUa_BadAggregateNotSupported
OpcUa_BadAggregateInvalidInputs = _opcuastatuscodes.OpcUa_BadAggregateInvalidInputs
OpcUa_BadAggregateConfigurationRejected = _opcuastatuscodes.OpcUa_BadAggregateConfigurationRejected
OpcUa_GoodDataIgnored = _opcuastatuscodes.OpcUa_GoodDataIgnored
OpcUa_BadRequestNotAllowed = _opcuastatuscodes.OpcUa_BadRequestNotAllowed
OpcUa_GoodEdited = _opcuastatuscodes.OpcUa_GoodEdited
OpcUa_GoodPostActionFailed = _opcuastatuscodes.OpcUa_GoodPostActionFailed
OpcUa_UncertainDominantValueChanged = _opcuastatuscodes.OpcUa_UncertainDominantValueChanged
OpcUa_GoodDependentValueChanged = _opcuastatuscodes.OpcUa_GoodDependentValueChanged
OpcUa_BadDominantValueChanged = _opcuastatuscodes.OpcUa_BadDominantValueChanged
OpcUa_UncertainDependentValueChanged = _opcuastatuscodes.OpcUa_UncertainDependentValueChanged
OpcUa_BadDependentValueChanged = _opcuastatuscodes.OpcUa_BadDependentValueChanged
OpcUa_GoodCommunicationEvent = _opcuastatuscodes.OpcUa_GoodCommunicationEvent
OpcUa_GoodShutdownEvent = _opcuastatuscodes.OpcUa_GoodShutdownEvent
OpcUa_GoodCallAgain = _opcuastatuscodes.OpcUa_GoodCallAgain
OpcUa_GoodNonCriticalTimeout = _opcuastatuscodes.OpcUa_GoodNonCriticalTimeout
OpcUa_BadInvalidArgument = _opcuastatuscodes.OpcUa_BadInvalidArgument
OpcUa_BadConnectionRejected = _opcuastatuscodes.OpcUa_BadConnectionRejected
OpcUa_BadDisconnect = _opcuastatuscodes.OpcUa_BadDisconnect
OpcUa_BadConnectionClosed = _opcuastatuscodes.OpcUa_BadConnectionClosed
OpcUa_BadInvalidState = _opcuastatuscodes.OpcUa_BadInvalidState
OpcUa_BadEndOfStream = _opcuastatuscodes.OpcUa_BadEndOfStream
OpcUa_BadNoDataAvailable = _opcuastatuscodes.OpcUa_BadNoDataAvailable
OpcUa_BadWaitingForResponse = _opcuastatuscodes.OpcUa_BadWaitingForResponse
OpcUa_BadOperationAbandoned = _opcuastatuscodes.OpcUa_BadOperationAbandoned
OpcUa_BadExpectedStreamToBlock = _opcuastatuscodes.OpcUa_BadExpectedStreamToBlock
OpcUa_BadWouldBlock = _opcuastatuscodes.OpcUa_BadWouldBlock
OpcUa_BadSyntaxError = _opcuastatuscodes.OpcUa_BadSyntaxError
OpcUa_BadMaxConnectionsReached = _opcuastatuscodes.OpcUa_BadMaxConnectionsReached
OpcUa_Good = _opcuastatuscodes.OpcUa_Good
OpcUa_Uncertain = _opcuastatuscodes.OpcUa_Uncertain
OpcUa_Bad = _opcuastatuscodes.OpcUa_Bad
# This file is compatible with both classic and new-style classes.


